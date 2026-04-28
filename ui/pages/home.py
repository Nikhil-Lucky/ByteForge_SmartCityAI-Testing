"""
Dashboard / Home Page
Author: Sunay (Team ByteForge)
"""

import streamlit as st
from ui.styles import render_hero_banner, render_feature_grid, render_smart_card


def render_home_page():
    """Render the main dashboard / home page."""

    st.markdown(render_hero_banner(
        "🏙️ SmartCity AI",
        "Your intelligent multi-agent assistant for real-time civic decision making in Bengaluru"
    ), unsafe_allow_html=True)

    features = [
        {"icon": "🚑", "title": "Emergency Response", "desc": "Instant ambulance dispatch, hospital bed tracking, and optimized routing with live ETA."},
        {"icon": "🛣️", "title": "Smart Traffic Advisor", "desc": "AI-powered route suggestions with real-time traffic, weather, and flood awareness."},
        {"icon": "📢", "title": "Civic Complaint Manager", "desc": "Auto-classify and track complaints — potholes, garbage, water, electricity issues."},
        {"icon": "🗺️", "title": "Live City Map", "desc": "Interactive map with ambulance tracking, traffic zones, and complaint hotspots."},
        {"icon": "🤖", "title": "Multi-Agent Intelligence", "desc": "Data, Analysis, Optimization & Explanation agents working together for smart recommendations."},
        {"icon": "💡", "title": "Explainable AI", "desc": "Every recommendation comes with a clear 'Why this suggestion?' explanation."},
    ]
    st.markdown(render_feature_grid(features), unsafe_allow_html=True)

    st.divider()

    st.markdown('<div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; color:#64748b; font-weight:600; margin-bottom:0.8rem;">📊 Live City Overview — Bengaluru</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🚑 Free Ambulances", "3", delta="1 dispatched", delta_color="inverse")
    with col2:
        st.metric("🏥 Hospital Beds", "47 available", delta="+5 since 1hr")
    with col3:
        st.metric("🚦 Avg. Congestion", "Medium", delta="-12% from peak")
    with col4:
        st.metric("📢 Open Complaints", "27", delta="3 new today")

    st.divider()

    st.subheader("⚙️ How SmartCity AI Works")

    how_cols = st.columns(4)
    steps = [
        ("1️⃣", "You Ask", "Type your query in natural language — English or Hinglish"),
        ("2️⃣", "Agents Analyze", "Multi-agent system fetches data, analyzes patterns, optimizes solutions"),
        ("3️⃣", "Smart Response", "Get actionable recommendations with maps and reasoning"),
        ("4️⃣", "Track & Resolve", "Monitor your requests, track ambulances, view complaint status"),
    ]

    for i, (num, title, desc) in enumerate(steps):
        with how_cols[i]:
            st.markdown(render_smart_card(num, title, "Step", desc), unsafe_allow_html=True)

    st.divider()

    st.subheader("💡 Try These Queries")

    example_cols = st.columns(2)
    with example_cols[0]:
        st.info("**Emergency:**\n- \"I need an ambulance in Jayanagar 3rd Block\"\n- \"Hospital beds available near BSK?\"\n- \"Accident on Bannerghatta Road — send help\"")
        st.info("**Traffic:**\n- \"Best route to Majestic from Jayanagar now\"\n- \"Is there flooding on Hosur Road?\"\n- \"Traffic update for Silk Board junction\"")
    with example_cols[1]:
        st.info("**Civic Issues:**\n- \"Pothole in Jayanagar 7th Block main road\"\n- \"Garbage not collected in 4th Block\"\n- \"Street light broken near park\"")
        st.info("**General:**\n- \"Weather forecast for Bengaluru today\"\n- \"Water supply schedule in Jayanagar\"\n- \"Power cut status in my area\"")
