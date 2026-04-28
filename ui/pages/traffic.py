"""
Traffic & Routes Page
Author: Sunay (Team ByteForge)
"""

import streamlit as st
import time
from ui.styles import render_smart_card, render_status_badge

MOCK_ROUTES = [
    {"name": "Via 100 Feet Road → Bannerghatta Road", "time": "28 mins", "distance": "12.3 km", "traffic": "Medium", "traffic_color": "warning", "weather_impact": "None", "recommended": True},
    {"name": "Via Hosur Road → Ring Road", "time": "35 mins", "distance": "14.1 km", "traffic": "Heavy", "traffic_color": "busy", "weather_impact": "Mild — drizzle expected", "recommended": False},
    {"name": "Via Kanakapura Road → Mysore Road", "time": "42 mins", "distance": "18.7 km", "traffic": "Low", "traffic_color": "online", "weather_impact": "None", "recommended": False},
]

MOCK_TRAFFIC_ZONES = [
    {"zone": "Silk Board Junction", "level": "Heavy", "status": "busy", "delay": "+18 min"},
    {"zone": "Jayanagar 4th Block", "level": "Medium", "status": "warning", "delay": "+5 min"},
    {"zone": "Banashankari Circle", "level": "Low", "status": "online", "delay": "+2 min"},
    {"zone": "Majestic Bus Stand", "level": "Heavy", "status": "busy", "delay": "+22 min"},
    {"zone": "KR Puram", "level": "Medium", "status": "warning", "delay": "+10 min"},
    {"zone": "Whitefield", "level": "Heavy", "status": "busy", "delay": "+25 min"},
]


def render_traffic_page():
    st.markdown('<div style="display:flex; align-items:center; gap:12px; margin-bottom:0.5rem;"><div style="font-size:2.2rem; width:56px; height:56px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, rgba(245,158,11,0.15), rgba(249,115,22,0.15)); border-radius:16px; border:1px solid rgba(245,158,11,0.2);">🛣️</div><div><div style="font-size:1.5rem; font-weight:700; color:#f1f5f9;">Smart Traffic & Route Advisor</div><div style="font-size:0.85rem; color:#94a3b8;">AI-powered routing with traffic, weather & flood awareness</div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    traffic_tabs = st.tabs(["🧭 Route Finder", "🚦 Traffic Zones", "🌧️ Weather Impact"])

    with traffic_tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            origin = st.text_input("📍 From", value="Jayanagar", key="traffic_from")
        with col2:
            destination = st.text_input("📍 To", value="Majestic", key="traffic_to")

        pref_col1, pref_col2 = st.columns(2)
        with pref_col1:
            travel_mode = st.selectbox("🚗 Mode", ["Car", "Bike", "Bus", "Walk"], key="travel_mode")
        with pref_col2:
            avoid = st.multiselect("⚠️ Avoid", ["Tolls", "Highways", "Waterlogged Areas"], key="avoid_opts")

        if st.button("🔍 Find Best Route", key="find_route", use_container_width=True):
            with st.spinner("🛣️ Analyzing traffic patterns..."):
                time.sleep(1)
                st.success(f"✅ **3 routes found** from {origin} to {destination}")

                for i, route in enumerate(MOCK_ROUTES):
                    badge_text = "⭐ RECOMMENDED" if route["recommended"] else f"Option {i + 1}"
                    badge_status = "online" if route["recommended"] else route["traffic_color"]
                    border = "border-left: 3px solid #10b981;" if route["recommended"] else ""
                    icon = "🟢" if route["recommended"] else "🟡"

                    st.markdown(render_smart_card(icon, route["name"], render_status_badge(badge_text, badge_status),
                        f'<div style="display:flex; gap:2rem; flex-wrap:wrap; margin-top:0.5rem;"><div>⏱️ <strong>{route["time"]}</strong></div><div>📏 {route["distance"]}</div><div>🚦 Traffic: {render_status_badge(route["traffic"], route["traffic_color"])}</div><div>🌧️ Weather: {route["weather_impact"]}</div></div>'
                    ), unsafe_allow_html=True)

                with st.expander("💡 Why this route?", expanded=True):
                    st.markdown("**Decision Reasoning:**\n1. **100 Feet Road** has 25% less congestion\n2. **No waterlogging** on recommended route\n3. **Silk Board** (alternate) has +18 min delay\n4. Weather clear on primary; drizzle on Hosur Road\n5. Third option adds 6.4 km extra distance")

    with traffic_tabs[1]:
        st.markdown("### 🚦 Real-Time Traffic Zone Monitor")
        for zone in MOCK_TRAFFIC_ZONES:
            zcol1, zcol2, zcol3 = st.columns([3, 1, 1])
            with zcol1:
                st.markdown(f"**{zone['zone']}**")
            with zcol2:
                st.markdown(render_status_badge(zone["level"], zone["status"]), unsafe_allow_html=True)
            with zcol3:
                st.markdown(f"⏱️ {zone['delay']}")

    with traffic_tabs[2]:
        st.markdown("### 🌧️ Weather Impact on Routes")
        wi_col1, wi_col2 = st.columns(2)
        with wi_col1:
            st.markdown(render_smart_card("🌤️", "Current Weather", "Bengaluru",
                '<div>🌡️ Temperature: <strong>29°C</strong></div><div>💧 Humidity: <strong>62%</strong></div><div>🌧️ Rain: <strong>15% probability</strong></div><div>💨 Wind: <strong>12 km/h NE</strong></div>'
            ), unsafe_allow_html=True)
        with wi_col2:
            st.markdown(render_smart_card("⚠️", "Flood Risk Zones", "Updated 30 min ago",
                '<div>🔴 <strong>Silk Board Underpass</strong> — High risk</div><div>🟡 <strong>Koramangala 80 Feet Road</strong> — Moderate</div><div>🟢 <strong>Jayanagar area</strong> — Low risk</div>'
            ), unsafe_allow_html=True)
        st.info("💡 Enable 'Avoid Waterlogged Areas' in Route Finder to auto-reroute during rain.")
