import random

# Base coordinates for Jayanagar, Bengaluru
BASE_LAT = 12.9250
BASE_LON = 77.5850

def get_mock_hospitals():
    """Returns a list of mock hospitals with bed availability around Jayanagar."""
    return [
        {
            "id": "H001",
            "name": "Jayanagar General Hospital",
            "lat": BASE_LAT + 0.005,
            "lon": BASE_LON + 0.002,
            "beds_available": random.randint(5, 20),
            "type": "Government"
        },
        {
            "id": "H002",
            "name": "Apollo Speciality Hospital",
            "lat": BASE_LAT - 0.008,
            "lon": BASE_LON + 0.005,
            "beds_available": random.randint(0, 10),
            "type": "Private"
        },
        {
            "id": "H003",
            "name": "Sagar Hospitals",
            "lat": BASE_LAT + 0.010,
            "lon": BASE_LON - 0.006,
            "beds_available": random.randint(10, 30),
            "type": "Private"
        },
        {
            "id": "H004",
            "name": "Sri Jayadeva Institute",
            "lat": BASE_LAT - 0.003,
            "lon": BASE_LON - 0.010,
            "beds_available": random.randint(0, 5),
            "type": "Government"
        }
    ]

def get_mock_ambulances():
    """Returns a list of mock ambulances around Jayanagar."""
    return [
        {
            "id": "AMB001",
            "lat": BASE_LAT + 0.003,
            "lon": BASE_LON - 0.004,
            "status": "Available",
            "type": "ALS (Advanced Life Support)"
        },
        {
            "id": "AMB002",
            "lat": BASE_LAT - 0.006,
            "lon": BASE_LON + 0.008,
            "status": "Busy",
            "type": "BLS (Basic Life Support)"
        },
        {
            "id": "AMB003",
            "lat": BASE_LAT + 0.008,
            "lon": BASE_LON + 0.007,
            "status": "Available",
            "type": "ICU on Wheels"
        }
    ]
