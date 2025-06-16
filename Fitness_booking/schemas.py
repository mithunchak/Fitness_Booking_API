from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class ClassCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Class name")
    dateTime: str = Field(..., description="Class date and time in IST (ISO format)")
    instructor: str = Field(..., min_length=1, max_length=100, description="Instructor name")
    availableSlots: int = Field(..., gt=0, le=100, description="Number of available slots")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Morning Yoga",
                "dateTime": "2025-06-16T06:00:00+05:30",
                "instructor": "Priya Sharma",
                "availableSlots": 20
            }
        }

class ClassResponse(BaseModel):
    id: str
    name: str
    dateTime: str
    instructor: str
    availableSlots: int
    totalSlots: int
    
    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    class_id: str = Field(..., description="ID of the class to book")
    client_name: str = Field(..., min_length=1, max_length=100, description="Client full name")
    client_email: str = Field(..., description="Client email address")
    
    class Config:
        schema_extra = {
            "example": {
                "class_id": "123e4567-e89b-12d3-a456-426614174000",
                "client_name": "Rahul Kumar",
                "client_email": "rahul@example.com"
            }
        }

class BookingResponse(BaseModel):
    id: str
    class_id: str
    class_name: str
    client_name: str
    client_email: str
    booking_time: str
    class_datetime: str
    
    class Config:
        from_attributes = True