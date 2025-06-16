import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
import tempfile
import os

# Override database for testing
os.environ["DATABASE_URL"] = "sqlite:///./test_fitness_booking.db"

from main import app
from database import engine, Base

# Create test database
Base.metadata.create_all(bind=engine)

client = TestClient(app)

class TestFitnessAPI:
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
    
    def test_create_class(self):
        """Test creating a fitness class"""
        class_data = {
            "name": "Test Yoga Class",
            "dateTime": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT10:00:00+05:30"),
            "instructor": "Test Instructor",
            "availableSlots": 10
        }
        
        response = client.post("/classes", json=class_data)
        assert response.status_code == 201
        
        created_class = response.json()
        assert created_class["name"] == class_data["name"]
        assert created_class["instructor"] == class_data["instructor"]
        assert created_class["availableSlots"] == class_data["availableSlots"]
        
        return created_class
    
    def test_get_classes(self):
        """Test getting all classes"""
        # First create a class
        self.test_create_class()
        
        response = client.get("/classes")
        assert response.status_code == 200
        
        classes = response.json()
        assert len(classes) > 0
    
    def test_book_class(self):
        """Test booking a class"""
        # First create a class
        created_class = self.test_create_class()
        
        booking_data = {
            "class_id": created_class["id"],
            "client_name": "Test User",
            "client_email": "test@example.com"
        }
        
        response = client.post("/book", json=booking_data)
        assert response.status_code == 201
        
        booking = response.json()
        assert booking["client_name"] == booking_data["client_name"]
        assert booking["client_email"] == booking_data["client_email"]
        
        return booking
    
    def test_get_bookings(self):
        """Test getting user bookings"""
        # First make a booking
        booking = self.test_book_class()
        
        response = client.get(f"/bookings?email={booking['client_email']}")
        assert response.status_code == 200
        
        bookings = response.json()
        assert len(bookings) > 0
        assert bookings[0]["client_email"] == booking["client_email"]
    
    def test_duplicate_booking_prevention(self):
        """Test that duplicate bookings are prevented"""
        created_class = self.test_create_class()
        
        booking_data = {
            "class_id": created_class["id"],
            "client_name": "Test User",
            "client_email": "duplicate@example.com"
        }
        
        # First booking should succeed
        response1 = client.post("/book", json=booking_data)
        assert response1.status_code == 201
        
        # Second booking should fail
        response2 = client.post("/book", json=booking_data)
        assert response2.status_code == 400
        assert "already booked" in response2.json()["detail"]
    
    def test_invalid_class_booking(self):
        """Test booking non-existent class"""
        booking_data = {
            "class_id": "non-existent-id",
            "client_name": "Test User",
            "client_email": "test@example.com"
        }
        
        response = client.post("/book", json=booking_data)
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])