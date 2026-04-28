import streamlit as st
import json
from datetime import datetime
from streamlit_folium import st_folium
from utils.map_utils import generate_live_city_map, generate_emergency_response_map

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

st.divider()

if page == "🗺️ Live Map":
    # ====================== LIVE MAP INTERFACE ======================
    st.subheader("🗺️ Live City Map")
    st.markdown("Real-time view of ambulances and hospitals in Bengaluru.")
    
    with st.spinner("Loading live map data..."):
        m = generate_live_city_map()
        st_folium(m, width=1200, height=600, returned_objects=[])

else:
    # ====================== MAIN CHAT INTERFACE ======================
    st.subheader("💬 Ask Anything (Natural Language)")
    
    user_query = st.text_input(
        "Type your message here...", 
        placeholder="I need ambulance in Jayanagar 3rd Block...",
        key="user_input"
    )
    
    if st.button("Send", type="primary") and user_query:
        with st.spinner("Router Agent thinking..."):
            
            # Simple Router Logic (you can later replace with full LangGraph)
            query_lower = user_query.lower()
            
            if "ambulance" in query_lower or "hospital" in query_lower or "emergency" in query_lower:
                response = f"""
**🚑 Emergency Response**
    
✅ **Router Agent** detected emergency request.
    
- Nearest Ambulance: **AMB001** (Free)
- ETA: **8-10 minutes**
- Recommended Hospital: **Jayanagar General Hospital** (14 beds available)
- Live tracking activated on map below
"""
                st.success(response)
                
                # Dynamic Folium Map for Emergency
                m = generate_emergency_response_map()
                st_folium(m, width=800, height=500, returned_objects=[])
                
            elif "route" in query_lower or "traffic" in query_lower or "go to" in query_lower or "majestic" in query_lower:
                response = f"""
**🛣️ Smart Route Advisor**
    
✅ Best Route Found!
    
- From: Jayanagar → To: Majestic
- Recommended Path: 100 Feet Road → Silk Board Flyover
- Estimated Time: **26 minutes**
- Traffic: Medium | Saves **15 minutes** compared to usual route
"""
                st.success(response)
                
            elif "pothole" in query_lower or "garbage" in query_lower or "water" in query_lower or "power" in query_lower or "complaint" in query_lower:
                comp_id = f"COMP-{datetime.now().strftime('%H%M%S')}"
                response = f"""
**📢 Complaint Registered**
    
✅ Complaint ID: **{comp_id}**
    
- Issue: {user_query}
- Status: Forwarded to BBMP Ward 172
- Expected Resolution: 24-48 hours
- You will be notified when action is taken
"""
                st.success(response)
                
            else:
                # General / Router fallback
                response = f"""
**✅ SmartCity AI**
    
I understood your query: **{user_query}**
    
I'm a multi-agent system. I can help with:
- 🚑 Ambulance & Hospital
- 🛣️ Traffic & Best Routes  
- 📢 Civic Complaints (Pothole, Garbage, Water, Power)
- 🗺️ Live Map
    
Try more specific questions!
"""
                st.info(response)

# ====================== QUICK TABS (Still available) ======================
st.divider()
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🚑 Emergency Help"):
        st.info("Type in chat: 'Need ambulance...'")
with col2:
    if st.button("🛣️ Best Route"):
        st.info("Type in chat: 'Best way to Majestic...'")
with col3:
    if st.button("📢 Report Issue"):
        st.info("Type in chat: 'Pothole in 7th block...'")
with col4:
    if st.button("🗺️ Show Live Map"):
        st.info("Go to Live Map tab in sidebar")

st.caption("ByteForge_SmartCityAI • Hackathon 2026")