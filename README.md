# Fitness_Booking_API

A comprehensive fitness booking system API built with FastAPI, SQLite, and SQLAlchemy ORM that allows users to manage fitness classes, bookings, and schedules with advanced features like timezone intelligence and smart booking management.

Technologies Used

FastAPI - Modern, fast web framework for building APIs

SQLite - Lightweight, serverless database engine

SQLAlchemy ORM - Python SQL toolkit and Object-Relational Mapping

Pydantic - Data validation using Python type annotations

Uvicorn - ASGI web server implementation

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mithunchak/Fitness_Booking_API.git
cd Fitness_Booking_API
```

### 2. Create Virtual Environment for API

Create a virtual environment specifically for running the main API:

```bash
# Create virtual environment with Python 3.11
python3.11 -m venv fitness_api_env

# Activate the virtual environment
# On Windows:
fitness_api_env\Scripts\activate

# On macOS/Linux:
source fitness_api_env/bin/activate
```

### 3. Install Dependencies for API

```bash
pip install -r requirements.txt
```

### 4. Create Virtual Environment for Demo

Create a separate virtual environment for running the demo and tests:

```bash
# Create demo environment with Python 3.11
python3.11 -m venv fitness_demo_env

# Activate the demo environment
# On Windows:
fitness_demo_env\Scripts\activate

# On macOS/Linux:
source fitness_demo_env/bin/activate
```

### 5. Install Dependencies for Demo

```bash
pip install -r requirements.txt
# Install additional testing dependencies if needed
pip install pytest requests
```

## Running the Application

### Start the API Server

1. Activate the API virtual environment:
```bash
# On Windows:
fitness_api_env\Scripts\activate

# On macOS/Linux:
source fitness_api_env/bin/activate
```

2. Start the API server:
```bash
python main.py
```
The FastAPI server will be available at http://localhost:8000.

FastAPI Features Available:

📋 Interactive API Documentation: http://localhost:8000/docs (Swagger UI)
📚 Alternative Documentation: http://localhost:8000/redoc (ReDoc)
🔧 OpenAPI Schema: http://localhost:8000/openapi.json

![image](https://github.com/user-attachments/assets/5cbb2fc5-a663-4797-a75b-10ba9fa7396c)


### Run the Demo

**Important:** Make sure the API server is running on `http://localhost:8000` before running the demo.

1. Open a new terminal window/tab (keep the API server running)
2. Navigate to the project directory
3. Activate the demo virtual environment:
```bash
# On Windows:
fitness_demo_env\Scripts\activate

# On macOS/Linux:
source fitness_demo_env/bin/activate
```

4. Run the demo script to see all API functionalities and error handling:
```bash
python demo.py
```

The demo will automatically connect to the running API server and demonstrate all available features including:

- 🚀 **Comprehensive API Testing** - Health checks and functionality validation
- 📅 **Class Management** - Create, view, and manage fitness classes
- 🎯 **Smart Booking System** - Book classes with duplicate and overbooking prevention
- 🌍 **Timezone Intelligence** - Multi-timezone support with IST storage
- 🛡️ **Error Handling** - Input validation and graceful error responses
- 📊 **Real-time Analytics** - Database state tracking and booking statistics
- 🧪 **Edge Case Testing** - Comprehensive validation and security testing

**Expected Demo Output:**

https://github.com/user-attachments/assets/4a1ab509-ca2b-48b2-a673-21641a6413c0

## Demo Features

The `demo.py` script demonstrates the following API functionalities:

- **API Health Check**
  - Verify API server is running and healthy
  - Display server status and timestamp

- **Class Management**
  - Create fitness classes with validation
  - View all available classes in database
  - Real-time slot tracking and availability

- **Booking Operations**
  - Book fitness classes with duplicate prevention
  - View user bookings with details
  - Real-time booking updates

- **Timezone Intelligence**
  - Automatic IST-based time handling
  - Multi-timezone support and conversion
  - Dynamic timezone query testing

- **Error Handling and Validation**
  - Input validation errors (empty names, invalid dates)
  - Duplicate booking prevention
  - Overbooking prevention with capacity limits
  - Invalid class ID handling
  - Email format validation
  - Required field validation

- **Advanced Features**
  - Database state tracking
  - Booking statistics and analytics
  - Comprehensive test reporting
  - Performance monitoring

## API Endpoints

The demo will test the following endpoints:

- `POST /classes` - Create fitness class
- `GET /classes` - Get all available classes
- `POST /book` - Book a fitness class
- `GET /bookings` - Get user bookings
- `GET /health` - API health check


### Manual Testing with Demo

The demo script includes comprehensive testing scenarios with detailed output:

```bash
python demo.py  # Run full comprehensive demo
```

**Demo Coverage:**
- ✅ API Health Check and Server Status
- ✅ Class Creation with Validation Testing
- ✅ Database State Tracking
- ✅ Timezone Conversion Testing
- ✅ Booking System with Duplicate Prevention
- ✅ Overbooking Prevention
- ✅ Input Validation and Error Handling
- ✅ Real-time Analytics and Statistics
- ✅ Comprehensive Test Reporting

## Troubleshooting

### Common Issues

1. **Python 3.11 not found**
   - Install Python 3.11 from python.org
   - Verify installation: `python3.11 --version`

2. **Virtual environment activation fails**
   - Check the correct path for your OS
   - Ensure you're in the project directory

3. **Dependencies installation fails**
   - Upgrade pip: `pip install --upgrade pip`
   - Check requirements.txt exists

4. **API connection errors in demo**
   - Ensure the API server is running
   - Check the correct port and host settings
   - Verify firewall/antivirus settings

5. **Database connection issues**
   - Check database configuration
   - Ensure database server is running
   - Verify connection credentials

### Getting Help

If you encounter issues:

1. Check the console output for error messages
2. Verify all dependencies are installed correctly
3. Ensure both virtual environments are properly configured
4. Check that the API server is running before executing the demo

## Project Structure

```
Fitness_Booking_API/
├── __pycache__/           # Python cache files
├── .pytest_cache/         # Pytest cache files  
├── database.py           # Database configuration and models
├── demo.py              # Demo script with comprehensive API testing
├── fitness_api.log      # API logging file
├── fitness_booking.db   # SQLite database file
├── fitness_booking.sqlpro # Database backup/export
├── main.py              # Main API application server
├── models.py            # Pydantic data models and schemas
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── schemas.py           # API request/response schemas
├── test_api.py          # API unit tests
├── fitness_api_env/     # API virtual environment
├── fitness_demo_env/    # Demo virtual environment
└── .gitignore           # Git ignore file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the demo to ensure functionality
5. Submit a pull request

