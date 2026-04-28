import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SmartCity AI", layout="wide", page_icon="🏙️")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.image("https://via.placeholder.com/150/00BFFF/FFFFFF?text=ByteForge", width=150)
    st.title("🧭 Navigation")
    page = st.radio("Quick Access", 
        ["🏠 Home", "🚑 Emergency", "🛣️ Traffic", "📢 Complaints", "🗺️ Live Map"])

# ====================== HEADER ======================
st.title("🏙️ SmartCity AI")
st.subheader("Intelligent Multi-Agent Assistant for Bengaluru")
st.caption("**Team ByteForge** • Real-time Civic Decision Making")

# ====================== MAIN INTELLIGENT CHAT ======================
st.divider()
st.subheader("💬 Ask SmartCity AI (Multi-Agent System)")

user_query = st.text_input(
    "Type your message here...", 
    placeholder="I need ambulance in Jayanagar 3rd Block...",
    key="user_input"
)

if st.button("Send", type="primary") and user_query:
    with st.spinner("🤖 Router Agent → Data Agent → Optimizer Agent working..."):
        
        query_lower = user_query.lower()
        
        if "ambulance" in query_lower or "hospital" in query_lower or "emergency" in query_lower:
            st.success("🚑 **Emergency Module Activated**")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Ambulance", "AMB001")
                st.metric("ETA", "8 minutes")
            with col2:
                st.metric("Hospital", "Jayanagar General")
                st.metric("Beds Free", "14")
            
            st.info("📍 **Mock Live Tracking Started**")
            st.map(pd.DataFrame([{"lat": 12.9250, "lon": 77.5850}]), use_container_width=True)
            
        elif "route" in query_lower or "traffic" in query_lower or "majestic" in query_lower:
            st.success("🛣️ **Route Optimizer Agent** Activated")
            st.write("**Best Route**: Jayanagar → 100 Feet Road → Silk Board")
            st.write("**Time**: 26 mins | **Traffic**: Medium")
            
        elif any(x in query_lower for x in ["pothole", "garbage", "water", "power", "light", "complaint"]):
            comp_id = f"COMP-{datetime.now().strftime('%H%M%S')}"
            st.success("📢 **Complaint Agent** Activated")
            st.write(f"**Complaint ID**: {comp_id}")
            st.write("Status: Forwarded to BBMP Ward 172")
            st.write("Expected Resolution: 24-48 hours")
            
        else:
            st.info(f"""
            ✅ **Router Agent** received: **{user_query}**

            I am a **Multi-Agent System**:
            - Router Agent → Decides category
            - Data Agent → Fetches real-time info
            - Optimizer Agent → Gives best solution
            - Explainer Agent → Explains why

            Try: ambulance, route, pothole, etc.
            """)

# Quick Actions
st.divider()
st.subheader("Quick Actions")
cols = st.columns(4)
with cols[0]:
    if st.button("🚑 Ambulance"):
        st.info("Type: I need ambulance...")
with cols[1]:
    if st.button("🛣️ Best Route"):
        st.info("Type: Best route to Majestic...")
with cols[2]:
    if st.button("📢 Report Issue"):
        st.info("Type: Pothole in 7th block...")
with cols[3]:
    if st.button("🗺️ Live Map"):
        st.switch_page("🗺️ Live Map") if "🗺️ Live Map" in st.session_state else st.info("Go to Live Map tab")

st.caption("ByteForge_SmartCityAI • Testing Version | Multi-Agent Ready")