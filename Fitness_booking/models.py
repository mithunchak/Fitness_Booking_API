from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Class(Base):
    __tablename__ = "fitness_classes"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    datetime_utc = Column(DateTime, nullable=False)
    instructor = Column(String, nullable=False)
    available_slots = Column(Integer, nullable=False)
    total_slots = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    bookings = relationship("Booking", back_populates="fitness_class")

class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(String, primary_key=True, index=True)
    class_id = Column(String, ForeignKey("fitness_classes.id"))
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    booking_time = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    fitness_class = relationship("Class", back_populates="bookings")