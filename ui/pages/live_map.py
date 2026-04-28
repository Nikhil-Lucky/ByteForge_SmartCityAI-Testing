"""
Live City Map Page
Author: Sunay (Team ByteForge)
NOTE: Full map + ambulance tracking by Suhas.
"""

import streamlit as st
import folium
from streamlit_folium import st_folium
from ui.styles import render_status_badge

MOCK_AMBULANCES = [
    {"id": "AMB001", "lat": 12.9250, "lon": 77.5850, "status": "Free", "hospital": "Jayanagar General", "type": "ALS"},
    {"id": "AMB002", "lat": 12.9300, "lon": 77.5800, "status": "Busy", "hospital": "Sagar Hospital", "type": "BLS"},
    {"id": "AMB003", "lat": 12.9200, "lon": 77.5900, "status": "Free", "hospital": "Manipal Hospital", "type": "ALS"},
    {"id": "AMB004", "lat": 12.9350, "lon": 77.5750, "status": "Free", "hospital": "Apollo Hospital", "type": "BLS"},
    {"id": "AMB005", "lat": 12.9180, "lon": 77.5920, "status": "Busy", "hospital": "Fortis Hospital", "type": "ALS"},
]

MOCK_COMPLAINTS_MAP = [
    {"lat": 12.9260, "lon": 77.5830, "type": "Pothole", "area": "7th Block"},
    {"lat": 12.9230, "lon": 77.5870, "type": "Garbage", "area": "4th Block"},
    {"lat": 12.9290, "lon": 77.5810, "type": "Street Light", "area": "3rd Block"},
    {"lat": 12.9210, "lon": 77.5890, "type": "Water Supply", "area": "5th Block"},
]

MOCK_HOSPITALS_MAP = [
    {"lat": 12.9255, "lon": 77.5855, "name": "Jayanagar General Hospital", "beds": 12},
    {"lat": 12.9310, "lon": 77.5790, "name": "Sagar Hospital", "beds": 8},
    {"lat": 12.9190, "lon": 77.5910, "name": "Manipal Hospital", "beds": 15},
]


def render_live_map_page():
    st.markdown('<div style="display:flex; align-items:center; gap:12px; margin-bottom:0.5rem;"><div style="font-size:2.2rem; width:56px; height:56px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, rgba(6,182,212,0.15), rgba(16,185,129,0.15)); border-radius:16px; border:1px solid rgba(6,182,212,0.2);">🗺️</div><div><div style="font-size:1.5rem; font-weight:700; color:#f1f5f9;">Live City Map</div><div style="font-size:0.85rem; color:#94a3b8;">Interactive map with ambulances, hospitals, traffic & complaints <span style="margin-left:0.5rem;"><span class="pulse-dot"></span> Live</span></div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    ctrl_col1, ctrl_col2, ctrl_col3, ctrl_col4 = st.columns(4)
    with ctrl_col1:
        show_ambulances = st.checkbox("🚑 Ambulances", value=True, key="map_amb")
    with ctrl_col2:
        show_hospitals = st.checkbox("🏥 Hospitals", value=True, key="map_hosp")
    with ctrl_col3:
        show_complaints = st.checkbox("📢 Complaints", value=True, key="map_comp")
    with ctrl_col4:
        show_traffic = st.checkbox("🚦 Traffic Zones", value=False, key="map_traffic")

    m = folium.Map(location=[12.9250, 77.5850], zoom_start=14, tiles="CartoDB dark_matter")

    if show_ambulances:
        for amb in MOCK_AMBULANCES:
            color = "green" if amb["status"] == "Free" else "red"
            folium.Marker([amb["lat"], amb["lon"]],
                popup=f"<b>🚑 {amb['id']}</b><br>Status: {amb['status']}<br>Hospital: {amb['hospital']}<br>Type: {amb['type']}",
                tooltip=f"{amb['id']} — {amb['status']}",
                icon=folium.Icon(color=color, icon="plus-sign", prefix="glyphicon")
            ).add_to(m)

    if show_hospitals:
        for hosp in MOCK_HOSPITALS_MAP:
            folium.Marker([hosp["lat"], hosp["lon"]],
                popup=f"<b>🏥 {hosp['name']}</b><br>Beds: {hosp['beds']}",
                tooltip=hosp["name"],
                icon=folium.Icon(color="blue", icon="home", prefix="glyphicon")
            ).add_to(m)

    if show_complaints:
        for comp in MOCK_COMPLAINTS_MAP:
            folium.Marker([comp["lat"], comp["lon"]],
                popup=f"<b>📢 {comp['type']}</b><br>Area: {comp['area']}",
                tooltip=f"{comp['type']} — {comp['area']}",
                icon=folium.Icon(color="orange", icon="exclamation-sign", prefix="glyphicon")
            ).add_to(m)

    if show_traffic:
        folium.Circle(location=[12.9170, 77.6230], radius=400, color="#ef4444", fill=True, fill_opacity=0.2, popup="🚦 Silk Board — Heavy", tooltip="Heavy Traffic").add_to(m)
        folium.Circle(location=[12.9250, 77.5850], radius=500, color="#f59e0b", fill=True, fill_opacity=0.15, popup="🚦 Jayanagar — Medium", tooltip="Medium Traffic").add_to(m)

    st_folium(m, width=1200, height=550, key="main_city_map")

    st.markdown('<div style="display:flex; gap:1.5rem; flex-wrap:wrap; padding:0.8rem 1rem; background:rgba(17,24,39,0.7); border:1px solid rgba(255,255,255,0.06); border-radius:12px; margin-top:0.5rem;"><div style="font-size:0.8rem; font-weight:600; color:#94a3b8;">LEGEND:</div><div style="font-size:0.8rem; color:#94a3b8;">🟢 Free Ambulance</div><div style="font-size:0.8rem; color:#94a3b8;">🔴 Busy Ambulance</div><div style="font-size:0.8rem; color:#94a3b8;">🔵 Hospital</div><div style="font-size:0.8rem; color:#94a3b8;">🟠 Complaint</div><div style="font-size:0.8rem; color:#94a3b8;">⭕ Traffic Zone</div></div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("### 📊 Map Statistics")
    stat_cols = st.columns(4)
    with stat_cols[0]:
        st.metric("🚑 Free Ambulances", sum(1 for a in MOCK_AMBULANCES if a["status"] == "Free"))
    with stat_cols[1]:
        st.metric("🏥 Hospitals Shown", len(MOCK_HOSPITALS_MAP))
    with stat_cols[2]:
        st.metric("📢 Active Complaints", len(MOCK_COMPLAINTS_MAP))
    with stat_cols[3]:
        st.metric("🗺️ Coverage Area", "~5 km²")
    st.caption("🔄 Map data refreshes automatically • Full ambulance tracking by Suhas")
