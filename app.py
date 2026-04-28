import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import requests
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="SmartCity AI", layout="wide", page_icon="🏙️")

st.title("🏙️ SmartCity AI")
st.subheader("Intelligent Assistant for Bengaluru Citizens")
st.markdown("**Team ByteForge** | Real-time Civic Decision Making")

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x150/00BFFF/FFFFFF?text=ByteForge", width=150)
    st.title("Navigation")
    page = st.radio("Go to", ["🏠 Home", "🚑 Emergency", "🛣️ Traffic", "📢 Complaints", "🗺️ Live Map"])
    
    st.divider()
    st.caption("Made with ❤️ for Bengaluru")

# Mock Data
@st.cache_data
def load_mock_data():
    # Ambulances
    ambulances = [
        {"id": "AMB001", "location": [12.9250, 77.5850], "status": "Free", "hospital": "Jayanagar General"},
        {"id": "AMB002", "location": [12.9300, 77.5800], "status": "Busy", "hospital": "Sagar Hospital"},
        {"id": "AMB003", "location": [12.9200, 77.5900], "status": "Free", "hospital": "Manipal Hospital"},
    ]
    return ambulances

ambulances = load_mock_data()

# Main Content
if page == "🏠 Home":
    st.success("Welcome to SmartCity AI! Ask me anything about emergencies, traffic, or civic issues.")
    st.info("Example queries:\n• I need ambulance in Jayanagar 3rd Block\n• Best route to Majestic now\n• Pothole in 7th block")

elif page == "🚑 Emergency":
    st.header("🚑 Emergency Assistant")
    query = st.text_input("Describe your emergency:", placeholder="Need ambulance in Jayanagar...")
    
    if st.button("Get Help"):
        with st.spinner("Finding best resources..."):
            st.success("✅ Nearest Ambulance Found!")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Ambulance ID", "AMB001")
                st.metric("ETA", "9 minutes")
            with col2:
                st.metric("Recommended Hospital", "Jayanagar General")
                st.metric("Beds Available", "12")
            
            st.map(pd.DataFrame([{"lat": 12.9250, "lon": 77.5850}]))

elif page == "🛣️ Traffic":
    st.header("🛣️ Smart Route Advisor")
    origin = st.text_input("From:", "Jayanagar")
    destination = st.text_input("To:", "Majestic")
    if st.button("Find Best Route"):
        st.success("Best Route Found!")
        st.info("Route via 100 Feet Road • Time: 28 mins • Traffic: Medium")

elif page == "📢 Complaints":
    st.header("📢 Civic Complaint Manager")
    issue = st.text_input("Describe the issue:", "Pothole in Jayanagar 7th Block")
    if st.button("Register Complaint"):
        st.success(f"Complaint Registered! ID: COMP-{datetime.now().strftime('%H%M')}")
        st.info("Expected Resolution: 48 hours")

elif page == "🗺️ Live Map":
    st.header("🗺️ Live City Map")
    m = folium.Map(location=[12.9250, 77.5850], zoom_start=14)
    
    # Add ambulances
    for amb in ambulances:
        color = "green" if amb["status"] == "Free" else "red"
        folium.Marker(
            amb["location"],
            popup=f"Ambulance {amb['id']} - {amb['status']}",
            icon=folium.Icon(color=color, icon="ambulance", prefix="fa")
        ).add_to(m)
    
    st_folium(m, width=1200, height=600)

# Chat Interface (Your Main AI Part)
st.divider()
st.subheader("💬 Ask SmartCity AI")
user_input = st.text_input("Type your query here (e.g. Need ambulance...)", key="chat_input")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        # This is where your multi-agent logic will go
        response = f"✅ Understood: **{user_input}**\n\nI'm analyzing the best action using real-time data..."
        st.write(response)
        st.info("🔄 Multi-agent system is being built by Nikhil")

# Footer
st.caption("ByteForge_SmartCityAI • Hackathon 2026")