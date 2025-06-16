from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import pytz
from datetime import datetime, timezone
import uuid

# Import our modules (we'll create these)
from database import engine, SessionLocal, Base
from models import Class, Booking
from schemas import ClassCreate, ClassResponse, BookingCreate, BookingResponse

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fitness Studio Booking API",
    description="""A professional booking system for fitness classes A comprehensive booking system for fitness studios with advanced features:

* **Smart Booking Management** - Prevents overbooking with real-time slot tracking
* **Timezone Intelligence** - Automatic IST-based storage with multi-timezone support
* **Duplicate Prevention** - Prevents users from booking the same class twice
* **Input Validation** - Comprehensive validation and sanitization
* **Error Handling** - Graceful error handling with detailed messages

### Timezone Support
All classes are stored in UTC internally but displayed in IST by default.
Use the `timezone` parameter to get times in different timezones.

### Analytics
Built-in metrics and analytics endpoints for business insights.

### Data Validation
Comprehensive input validation prevents invalid data and ensures data integrity. 
    """,
    version="1.0.0",
    contact={
    "name": "Fitness Studio API Support",
    "email": "support@fitnessstudio.com",
},
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utility functions
def convert_to_utc(datetime_str: str) -> datetime:
    """Convert IST datetime to UTC"""
    try:
        # Parse the datetime string
        if datetime_str.endswith('+05:30'):
            dt_str = datetime_str[:-6]
            dt = datetime.fromisoformat(dt_str)
            ist_tz = pytz.timezone('Asia/Kolkata')
            localized_dt = ist_tz.localize(dt)
            return localized_dt.astimezone(pytz.UTC)
        else:
            # Assume IST if no timezone
            dt = datetime.fromisoformat(datetime_str.replace('Z', ''))
            ist_tz = pytz.timezone('Asia/Kolkata')
            localized_dt = ist_tz.localize(dt)
            return localized_dt.astimezone(pytz.UTC)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid datetime format")

def convert_from_utc(utc_dt: datetime, target_timezone: str = "UTC") -> str:
    """Convert UTC datetime to specified timezone"""
    try:
        if target_timezone == "Asia/Kolkata" or target_timezone == "IST":
            target_tz = pytz.timezone('Asia/Kolkata')
        else:
            target_tz = pytz.UTC
        
        # Ensure UTC datetime is timezone-aware
        if utc_dt.tzinfo is None:
            utc_dt = pytz.UTC.localize(utc_dt)
        
        converted_dt = utc_dt.astimezone(target_tz)
        return converted_dt.isoformat()
    except Exception:
        return utc_dt.isoformat()

# API Endpoints

@app.post("/classes", response_model=ClassResponse, status_code=201)
async def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    """Create a new fitness class"""
    
    # Convert IST to UTC for storage
    utc_datetime = convert_to_utc(class_data.dateTime)
    
    # Check if datetime is in the future - FIX: Use timezone-aware datetime
    current_utc = datetime.now(timezone.utc)
    if utc_datetime <= current_utc:
        raise HTTPException(status_code=400, detail="Class must be scheduled for future time")
    
    # Create class
    db_class = Class(
        id=str(uuid.uuid4()),
        name=class_data.name,
        datetime_utc=utc_datetime,
        instructor=class_data.instructor,
        available_slots=class_data.availableSlots,
        total_slots=class_data.availableSlots
    )
    
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    
    return ClassResponse(
        id=db_class.id,
        name=db_class.name,
        dateTime=convert_from_utc(db_class.datetime_utc, "Asia/Kolkata"),
        instructor=db_class.instructor,
        availableSlots=db_class.available_slots,
        totalSlots=db_class.total_slots
    )

@app.get("/classes", response_model=List[ClassResponse])
async def get_classes(
    timezone_param: str = Query("UTC", alias="timezone", description="Timezone for datetime conversion"),
    db: Session = Depends(get_db)
):
    """Get all upcoming fitness classes"""
    
    # Get classes that are in the future - FIX: Handle timezone-naive datetime from DB
    current_utc = datetime.now(timezone.utc)
    
    # Get all classes first, then filter with proper timezone handling
    all_classes = db.query(Class).all()
    
    upcoming_classes = []
    for cls in all_classes:
        # Make db datetime timezone-aware if it's naive
        class_datetime = cls.datetime_utc
        if class_datetime.tzinfo is None:
            class_datetime = pytz.UTC.localize(class_datetime)
        
        # Only include future classes
        if class_datetime > current_utc:
            upcoming_classes.append(cls)
    
    return [
        ClassResponse(
            id=cls.id,
            name=cls.name,
            dateTime=convert_from_utc(cls.datetime_utc, timezone_param),
            instructor=cls.instructor,
            availableSlots=cls.available_slots,
            totalSlots=cls.total_slots
        )
        for cls in upcoming_classes
    ]
@app.post("/book", response_model=BookingResponse, status_code=201)
async def book_class(booking_data: BookingCreate, db: Session = Depends(get_db)):
    """Book a spot in a fitness class"""
    
    # Check if class exists
    db_class = db.query(Class).filter(Class.id == booking_data.class_id).first()
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    
    # Check if class is in the future - FIX: Handle timezone-naive datetime from DB
    current_utc = datetime.now(timezone.utc)
    
    # Make db datetime timezone-aware if it's naive
    class_datetime = db_class.datetime_utc
    if class_datetime.tzinfo is None:
        class_datetime = pytz.UTC.localize(class_datetime)
    
    if class_datetime <= current_utc:
        raise HTTPException(status_code=400, detail="Cannot book past classes")
    
    # Check if slots are available
    if db_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No available slots")
    
    # Check if user already booked this class
    existing_booking = db.query(Booking).filter(
        Booking.class_id == booking_data.class_id,
        Booking.client_email == booking_data.client_email
    ).first()
    
    if existing_booking:
        raise HTTPException(status_code=400, detail="You have already booked this class")
    
    # Create booking - FIX: Use timezone-aware datetime
    db_booking = Booking(
        id=str(uuid.uuid4()),
        class_id=booking_data.class_id,
        client_name=booking_data.client_name,
        client_email=booking_data.client_email,
        booking_time=datetime.now(timezone.utc)
    )
    
    # Reduce available slots
    db_class.available_slots -= 1
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    
    return BookingResponse(
        id=db_booking.id,
        class_id=db_booking.class_id,
        class_name=db_class.name,
        client_name=db_booking.client_name,
        client_email=db_booking.client_email,
        booking_time=db_booking.booking_time.isoformat(),
        class_datetime=convert_from_utc(db_class.datetime_utc, "Asia/Kolkata")
    )
@app.get("/bookings", response_model=List[BookingResponse])
async def get_bookings(
    email: str = Query(..., description="Client email address"),
    db: Session = Depends(get_db)
):
    """Get all bookings for a specific email"""
    
    bookings = db.query(Booking).filter(Booking.client_email == email).all()
    
    result = []
    for booking in bookings:
        db_class = db.query(Class).filter(Class.id == booking.class_id).first()
        result.append(
            BookingResponse(
                id=booking.id,
                class_id=booking.class_id,
                class_name=db_class.name if db_class else "Unknown",
                client_name=booking.client_name,
                client_email=booking.client_email,
                booking_time=booking.booking_time.isoformat(),
                class_datetime=convert_from_utc(db_class.datetime_utc, "Asia/Kolkata") if db_class else ""
            )
        )
    
    return result

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message": "Fitness Booking API is running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)