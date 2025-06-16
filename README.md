# Fitness_Booking_API
# Fitness Booking API

A comprehensive fitness booking system API built with Python that allows users to manage fitness classes, bookings, and schedules.

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Fitness_Booking_API.git
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
python app.py
# or
python main.py
```

The API will be available at `http://localhost:8000`.

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
```
🚀 COMPREHENSIVE FITNESS BOOKING API DEMO
🔧 Testing All Requirements & Edge Cases
======================================================================
✅ API Health Check: healthy
   Timestamp: 2025-06-16T17:28:53.182787+00:00
   Message: Fitness Booking API is running

📋 Testing Fitness Class Creation
✅ [1] Created: Morning Yoga Flow
✅ [2] Created: Evening HIIT Training

🧪 Testing Invalid Class Creation Scenarios:
✅ [1] Correctly rejected: Empty class name
✅ [2] Correctly rejected: Past date/time
✅ [3] Correctly rejected: Invalid slot count

📋 Testing Booking Functionality
✅ [1] Booking confirmed: Mithun Kumar
✅ [2] Booking confirmed: Priya Patel

🔄 Testing Error Handling & Edge Cases:
✅ Duplicate booking correctly prevented
✅ Invalid class ID correctly handled
✅ Overbooking prevention working correctly

🎯 📊 COMPREHENSIVE TEST REPORT
============================================================
🎯 API Functionality Tests: ✅ ALL PASSED
🛡️ Error Handling Tests: ✅ ALL PASSED  
🔒 Security & Validation Tests: ✅ ALL PASSED
🌍 Timezone Features: ✅ ALL PASSED
📈 Performance & Edge Cases: ✅ ALL PASSED
```

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

## Testing

### Run Unit Tests

```bash
# In the demo environment
python -m pytest tests/
```

### Run Integration Tests

```bash
# In the demo environment
python -m pytest tests/integration/
```

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
├── app.py                 # Main API application
├── demo.py               # Demo script with API testing
├── requirements.txt      # Project dependencies
├── config.py            # Configuration settings
├── models/              # Data models
├── routes/              # API route handlers
├── tests/               # Test files
├── fitness_api_env/     # API virtual environment
├── fitness_demo_env/    # Demo virtual environment
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the demo to ensure functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
