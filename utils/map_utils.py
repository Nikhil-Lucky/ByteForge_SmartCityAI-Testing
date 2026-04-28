import folium
from geopy.distance import geodesic
from .mock_data import get_mock_hospitals, get_mock_ambulances, BASE_LAT, BASE_LON

def create_base_map(lat=BASE_LAT, lon=BASE_LON, zoom_start=14):
    """Creates a base folium map centered at the given coordinates."""
    m = folium.Map(location=[lat, lon], zoom_start=zoom_start, tiles="CartoDB positron")
    return m

def get_nearest_ambulance(user_lat, user_lon):
    """Finds the nearest available ambulance to the given coordinates."""
    ambulances = get_mock_ambulances()
    available_ambs = [a for a in ambulances if a["status"] == "Available"]
    
    if not available_ambs:
        return ambulances[0], 0 # Fallback
        
    nearest_amb = min(
        available_ambs, 
        key=lambda a: geodesic((user_lat, user_lon), (a["lat"], a["lon"])).km
    )
    distance_km = geodesic((user_lat, user_lon), (nearest_amb["lat"], nearest_amb["lon"])).km
    return nearest_amb, distance_km

def get_best_hospital(user_lat, user_lon):
    """Finds the nearest hospital with available beds."""
    hospitals = get_mock_hospitals()
    available_hosps = [h for h in hospitals if h["beds_available"] > 0]
    
    if not available_hosps:
        return hospitals[0], 0 # Fallback
        
    best_hosp = min(
        available_hosps,
        key=lambda h: geodesic((user_lat, user_lon), (h["lat"], h["lon"])).km
    )
    distance_km = geodesic((user_lat, user_lon), (best_hosp["lat"], best_hosp["lon"])).km
    return best_hosp, distance_km

def generate_live_city_map():
    """Generates a map with all hospitals and ambulances for the 'Live Map' view."""
    m = create_base_map()
    
    hospitals = get_mock_hospitals()
    ambulances = get_mock_ambulances()
    
    # Add hospitals
    for h in hospitals:
        color = "green" if h["beds_available"] > 5 else ("orange" if h["beds_available"] > 0 else "red")
        folium.Marker(
            location=[h["lat"], h["lon"]],
            popup=f"<b>{h['name']}</b><br>Beds: {h['beds_available']}<br>Type: {h['type']}",
            icon=folium.Icon(color=color, icon="plus", prefix="fa")
        ).add_to(m)
        
    # Add ambulances
    for a in ambulances:
        color = "blue" if a["status"] == "Available" else "gray"
        folium.Marker(
            location=[a["lat"], a["lon"]],
            popup=f"<b>{a['id']}</b><br>Status: {a['status']}<br>Type: {a['type']}",
            icon=folium.Icon(color=color, icon="ambulance", prefix="fa")
        ).add_to(m)
        
    return m

def generate_emergency_response_map(user_lat=BASE_LAT, user_lon=BASE_LON, assigned_amb=None, target_hosp=None):
    """Generates a map showing user location, assigned ambulance, and target hospital."""
    m = create_base_map(lat=user_lat, lon=user_lon, zoom_start=15)
    
    # Add User Location
    folium.Marker(
        location=[user_lat, user_lon],
        popup="<b>Emergency Location</b>",
        icon=folium.Icon(color="red", icon="user", prefix="fa")
    ).add_to(m)
    
    if assigned_amb:
        folium.Marker(
            location=[assigned_amb["lat"], assigned_amb["lon"]],
            popup=f"<b>{assigned_amb['id']} (On the way!)</b>",
            icon=folium.Icon(color="blue", icon="ambulance", prefix="fa")
        ).add_to(m)
    
    if target_hosp:
        folium.Marker(
            location=[target_hosp["lat"], target_hosp["lon"]],
            popup=f"<b>{target_hosp['name']}</b><br>Beds: {target_hosp['beds_available']}",
            icon=folium.Icon(color="green", icon="plus", prefix="fa")
        ).add_to(m)
    
    if assigned_amb and target_hosp:
        # Draw a simple line representing the route (mock route)
        route_coords = [
            [assigned_amb["lat"], assigned_amb["lon"]],
            [user_lat, user_lon],
            [target_hosp["lat"], target_hosp["lon"]]
        ]
        folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=0.8).add_to(m)
    
    return m
