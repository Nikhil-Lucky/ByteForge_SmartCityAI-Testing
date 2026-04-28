"""
Emergency Services Page
Author: Sunay (Team ByteForge)
"""

import streamlit as st
import pandas as pd
import time
from datetime import datetime
from ui.styles import render_smart_card, render_status_badge


MOCK_AMBULANCES = [
    {"id": "AMB001", "lat": 12.9250, "lon": 77.5850, "status": "Free", "hospital": "Jayanagar General Hospital", "type": "ALS", "eta_mins": 9},
    {"id": "AMB002", "lat": 12.9300, "lon": 77.5800, "status": "Busy", "hospital": "Sagar Hospital", "type": "BLS", "eta_mins": None},
    {"id": "AMB003", "lat": 12.9200, "lon": 77.5900, "status": "Free", "hospital": "Manipal Hospital", "type": "ALS", "eta_mins": 14},
    {"id": "AMB004", "lat": 12.9350, "lon": 77.5750, "status": "Free", "hospital": "Apollo Hospital", "type": "BLS", "eta_mins": 18},
    {"id": "AMB005", "lat": 12.9180, "lon": 77.5920, "status": "Busy", "hospital": "Fortis Hospital", "type": "ALS", "eta_mins": None},
]

MOCK_HOSPITALS = [
    {"name": "Jayanagar General Hospital", "beds": 12, "icu": 3, "distance": "1.2 km", "rating": 4.2},
    {"name": "Sagar Hospital", "beds": 8, "icu": 1, "distance": "2.1 km", "rating": 4.5},
    {"name": "Manipal Hospital", "beds": 15, "icu": 5, "distance": "3.4 km", "rating": 4.7},
    {"name": "Apollo Hospital", "beds": 20, "icu": 8, "distance": "4.8 km", "rating": 4.6},
    {"name": "Fortis Hospital", "beds": 6, "icu": 2, "distance": "5.2 km", "rating": 4.3},
]


def render_emergency_page():
    st.markdown('<div style="display:flex; align-items:center; gap:12px; margin-bottom:0.5rem;"><div style="font-size:2.2rem; width:56px; height:56px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, rgba(239,68,68,0.15), rgba(249,115,22,0.15)); border-radius:16px; border:1px solid rgba(239,68,68,0.2);">🚑</div><div><div style="font-size:1.5rem; font-weight:700; color:#f1f5f9;">Emergency Services</div><div style="font-size:0.85rem; color:#94a3b8;">Find ambulances, hospitals & dispatch emergency help</div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    emg_tabs = st.tabs(["🚑 Find Ambulance", "🏥 Hospital Beds", "📍 Track Dispatch"])

    with emg_tabs[0]:
        col_input, col_type = st.columns([3, 1])
        with col_input:
            location = st.text_input("📍 Your location or emergency address", placeholder="e.g., Jayanagar 3rd Block, 11th Main Road...", key="emg_location")
        with col_type:
            emg_type = st.selectbox("Emergency Type", ["Medical", "Accident", "Fire", "Other"], key="emg_type")

        if st.button("🚨 Find Nearest Ambulance", key="emg_find", use_container_width=True):
            with st.spinner("🔍 Scanning available ambulances..."):
                time.sleep(1)
                st.success("✅ **Ambulance Found & Dispatched!**")

                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.markdown(render_smart_card("🚑", "AMB001 — Dispatched", "Advanced Life Support (ALS)",
                        f'<div style="margin-top:0.5rem;"><div>📍 <strong>From:</strong> Jayanagar General Hospital</div><div>⏱️ <strong>ETA:</strong> 9 minutes</div><div>🛣️ <strong>Route:</strong> 11th Main → 100 Feet Road</div><div style="margin-top:0.5rem;">{render_status_badge("En Route", "warning")}</div></div>'
                    ), unsafe_allow_html=True)
                with res_col2:
                    st.markdown(render_smart_card("🏥", "Recommended Hospital", "Jayanagar General Hospital",
                        f'<div style="margin-top:0.5rem;"><div>🛏️ <strong>Beds:</strong> 12</div><div>🫀 <strong>ICU:</strong> 3</div><div>📏 <strong>Distance:</strong> 1.2 km</div><div>⭐ <strong>Rating:</strong> 4.2/5</div><div style="margin-top:0.5rem;">{render_status_badge("Accepting Patients", "online")}</div></div>'
                    ), unsafe_allow_html=True)

                with st.expander("💡 Why this recommendation?", expanded=True):
                    st.markdown("**Decision Reasoning:**\n1. **AMB001** is the closest free ambulance (1.2 km)\n2. It's an **ALS unit** — equipped for your emergency\n3. **Jayanagar General** has the most beds (12) with shortest distance\n4. Current route has **low traffic** (Green zone)\n5. AMB003 is backup at 14 min ETA")

                st.markdown("---")
                st.markdown("🗺️ **Live Ambulance Tracking Map** *(Full tracking by Suhas)*")
                st.map(pd.DataFrame({"lat": [12.9250, 12.9200], "lon": [77.5850, 77.5900]}), zoom=14)

    with emg_tabs[1]:
        st.markdown("### 🏥 Real-Time Hospital Bed Availability")
        st.caption("Data updates every 5 minutes • Showing hospitals near Jayanagar")
        for hosp in MOCK_HOSPITALS:
            cols = st.columns([3, 1, 1, 1, 1])
            with cols[0]:
                st.markdown(f"**{hosp['name']}**")
            with cols[1]:
                st.metric("Beds", hosp["beds"])
            with cols[2]:
                st.metric("ICU", hosp["icu"])
            with cols[3]:
                st.markdown(f"📏 {hosp['distance']}")
            with cols[4]:
                st.markdown(f"⭐ {hosp['rating']}")

    with emg_tabs[2]:
        st.markdown("### 📍 Active Dispatch Tracking")
        for amb in MOCK_AMBULANCES:
            if amb["status"] == "Busy":
                st.markdown(render_smart_card("🚑", f"{amb['id']} — In Transit", amb["hospital"],
                    f'<div>🏥 Hospital: <strong>{amb["hospital"]}</strong></div><div>📍 Position: ({amb["lat"]:.4f}, {amb["lon"]:.4f})</div><div>🔧 Type: <strong>{amb["type"]}</strong></div><div style="margin-top:0.5rem;">{render_status_badge("Busy — En Route", "busy")}</div>'
                ), unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🚑 All Ambulance Units — Status Board")
    amb_cols = st.columns(len(MOCK_AMBULANCES))
    for i, amb in enumerate(MOCK_AMBULANCES):
        with amb_cols[i]:
            badge = render_status_badge(amb["status"], "online" if amb["status"] == "Free" else "busy")
            st.markdown(render_smart_card("🚑", amb["id"], amb["hospital"],
                f'<div>Type: <strong>{amb["type"]}</strong></div><div>ETA: <strong>{amb["eta_mins"] or "—"} min</strong></div><div style="margin-top:0.5rem;">{badge}</div>'
            ), unsafe_allow_html=True)
