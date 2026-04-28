import streamlit as st
import pandas as pd
from datetime import datetime
import random
from streamlit_folium import st_folium
from utils.map_utils import generate_live_city_map, generate_emergency_response_map

st.set_page_config(page_title="SmartCity AI", layout="wide", page_icon="🏙️")

# ====================== AREA DATA ======================
AREA_COORDS = {
    "Jayanagar": (12.9250, 77.5938),
    "Koramangala": (12.9352, 77.6245),
    "Whitefield": (12.9698, 77.7500),
    "Electronic City": (12.8452, 77.6602),
    "Majestic": (12.9766, 77.5713),
    "Indiranagar": (12.9784, 77.6408),
    "HSR Layout": (12.9116, 77.6473),
    "BTM Layout": (12.9166, 77.6101),
    "Marathahalli": (12.9569, 77.7011),
    "Hebbal": (13.0358, 77.5970),
    "Yelahanka": (13.1007, 77.5963),
    "Bengaluru": (12.9716, 77.5946)
}

# ====================== HELPER FUNCTIONS ======================
def detect_area(user_query):
    query_lower = user_query.lower()

    area_keywords = {
        "jayanagar": "Jayanagar",
        "koramangala": "Koramangala",
        "whitefield": "Whitefield",
        "electronic city": "Electronic City",
        "majestic": "Majestic",
        "indiranagar": "Indiranagar",
        "hsr": "HSR Layout",
        "btm": "BTM Layout",
        "marathahalli": "Marathahalli",
        "hebbal": "Hebbal",
        "yelahanka": "Yelahanka"
    }

    for keyword, area in area_keywords.items():
        if keyword in query_lower:
            return area

    if "near me" in query_lower:
        return "Jayanagar"

    return "Bengaluru"


def detect_intent(user_query):
    query_lower = user_query.lower()

    if any(word in query_lower for word in ["ambulance", "accident", "emergency", "urgent"]):
        return "Emergency"

    if any(word in query_lower for word in ["hospital", "bed", "doctor", "clinic", "medical"]):
        return "Hospital"

    if any(word in query_lower for word in ["traffic", "route", "jam", "congestion", "go to", "best route"]):
        return "Traffic"

    if any(word in query_lower for word in ["pothole", "garbage", "waterlogging", "drainage", "street light", "power", "complaint", "water"]):
        return "Civic Complaint"

    if any(word in query_lower for word in ["ev", "charging", "charger", "battery", "electric vehicle"]):
        return "EV Charging"

    if any(word in query_lower for word in ["service", "repair", "honda", "bike", "car", "mechanic"]):
        return "Vehicle Service"

    return "General City Help"


def get_priority(intent):
    if intent == "Emergency":
        return "Critical", random.randint(90, 100)
    if intent == "Hospital":
        return "High", random.randint(75, 90)
    if intent == "Traffic":
        return "Medium", random.randint(55, 75)
    if intent == "Civic Complaint":
        return "Medium", random.randint(50, 80)
    if intent == "EV Charging":
        return "Normal", random.randint(35, 60)
    if intent == "Vehicle Service":
        return "Normal", random.randint(30, 55)

    return "Low", random.randint(20, 45)


def show_reasoning(intent, area, priority, score):
    st.info(f"""
🧠 **AI Decision Reasoning**

- Router Agent detected the request as **{intent}**
- Location Agent detected the area as **{area}**
- Priority Engine assigned **{priority} priority**
- Urgency Score: **{score}/100**
- Data Agent used mock city data for this prototype
- Optimizer Agent selected the best action for the citizen
""")


def show_simple_map(area):
    lat, lon = AREA_COORDS.get(area, AREA_COORDS["Bengaluru"])
    map_df = pd.DataFrame([{"lat": lat, "lon": lon}])
    st.map(map_df, use_container_width=True)


# ====================== SIDEBAR ======================
with st.sidebar:
    st.image("https://via.placeholder.com/150/00BFFF/FFFFFF?text=ByteForge", width=150)
    st.title("🧭 Navigation")
    page = st.radio(
        "Quick Access",
        ["🏠 Home", "🚑 Emergency", "🛣️ Traffic", "📢 Complaints", "🗺️ Live Map"]
    )

    st.divider()
    st.caption("Prototype Mode")
    st.write("Using mock civic data for hackathon demo.")

# ====================== HEADER ======================
st.title("🏙️ SmartCity AI")
st.subheader("Intelligent Multi-Agent Assistant for Bengaluru")
st.caption("**Team ByteForge** • Real-time Civic Decision Making")

# ====================== HOME DASHBOARD ======================
if page == "🏠 Home":
    st.divider()
    st.subheader("📊 Smart City Command Center")

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Ambulances", "8 Active")
    c2.metric("Hospitals", "12 Online")
    c3.metric("Open Complaints", "43")
    c4.metric("Traffic Hotspots", "6")
    c5.metric("Avg Response", "9 min")

# ====================== LIVE MAP PAGE ======================
if page == "🗺️ Live Map":
    st.divider()
    st.subheader("🗺️ Live City Map")
    st.markdown("Real-time prototype view of ambulances and hospitals in Bengaluru.")

    with st.spinner("Loading live map data..."):
        m = generate_live_city_map()
        st_folium(m, width=1200, height=600, returned_objects=[])

# ====================== MAIN CHAT INTERFACE ======================
st.divider()
st.subheader("💬 Ask SmartCity AI")

st.write(
    "Type any Bengaluru city problem or travel need. Example: ambulance, hospital beds, traffic, pothole, EV charging, service center, waterlogging, or nearby help."
)

user_query = st.text_input(
    "Type your message here...",
    placeholder="Example: I need ambulance in Jayanagar OR Find EV charging points near me",
    key="user_input"
)

if st.button("Send", type="primary") and user_query:
    with st.spinner("Router Agent → Location Agent → Data Agent → Optimizer Agent → Explainer Agent working..."):

        detected_area = detect_area(user_query)
        intent = detect_intent(user_query)
        priority, score = get_priority(intent)

        st.success(f"✅ **{intent} Agent Activated**")

        m1, m2, m3 = st.columns(3)
        m1.metric("Detected Intent", intent)
        m2.metric("Detected Area", detected_area)
        m3.metric("Priority Score", f"{score}/100")

        show_reasoning(intent, detected_area, priority, score)

        # ====================== EMERGENCY ======================
        if intent == "Emergency":
            st.subheader("🚑 Emergency Response")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Nearest Ambulance", "AMB001")
                st.metric("ETA", "8-10 minutes")
                st.write("Status: Available")

            with col2:
                st.metric("Recommended Hospital", f"{detected_area} General Hospital")
                st.metric("Beds Available", random.randint(8, 25))
                st.write("Emergency Support: Yes")

            st.warning("AI Action: Dispatch the nearest ambulance and route the patient to a hospital with available beds.")

            try:
                m = generate_emergency_response_map()
                st_folium(m, width=900, height=500, returned_objects=[])
            except Exception:
                show_simple_map(detected_area)

        # ====================== HOSPITAL ======================
        elif intent == "Hospital":
            st.subheader("🏥 Hospital Bed Finder")

            hospital_data = pd.DataFrame([
                [f"{detected_area} General Hospital", random.randint(8, 20), "Available", "Yes"],
                [f"CityCare Hospital {detected_area}", random.randint(2, 12), "Available", "Limited"],
                [f"LifeLine Medical Center {detected_area}", random.randint(1, 10), "Busy", "Yes"]
            ], columns=["Hospital", "Beds Available", "Status", "Emergency Support"])

            st.dataframe(hospital_data, use_container_width=True)
            st.success("AI Suggestion: Choose the hospital with maximum available beds and emergency support.")
            show_simple_map(detected_area)

        # ====================== TRAFFIC ======================
        elif intent == "Traffic":
            st.subheader("🛣️ Smart Route Advisor")

            st.write(f"**Area:** {detected_area}")
            st.write("**Traffic Condition:** Medium to Heavy")
            st.write("**Estimated Time:** 22-35 minutes")
            st.write("**Alternative Route:** Available")
            st.write(f"**Suggested Action:** Avoid the main junction near {detected_area} and use inner roads.")

            st.warning("AI Action: Route optimized based on congestion, estimated delay, and travel safety.")
            show_simple_map(detected_area)

        # ====================== CIVIC COMPLAINT ======================
        elif intent == "Civic Complaint":
            comp_id = f"COMP-{datetime.now().strftime('%H%M%S')}"

            st.subheader("📢 Civic Complaint Registered")

            st.write(f"**Complaint ID:** {comp_id}")
            st.write(f"**Issue:** {user_query}")
            st.write(f"**Area:** {detected_area}")
            st.write("**Status:** Forwarded to BBMP Ward Office")
            st.write("**Expected Resolution:** 24-48 hours")
            st.write(f"**Priority:** {priority}")

            st.success("AI Action: Complaint categorized, prioritized, and forwarded to the responsible civic department.")
            show_simple_map(detected_area)

        # ====================== EV CHARGING ======================
        elif intent == "EV Charging":
            st.subheader("🔋 EV Charging Assistant")

            ev_data = pd.DataFrame([
                ["BESCOM EV Charging Station", "1.2 km", "Fast Charger", "2 slots available", "Open"],
                ["Ather Grid Point", "2.1 km", "2-Wheeler Fast Charger", "1 slot available", "Open"],
                ["Tata Power EZ Charge", "3.4 km", "4-Wheeler DC Charger", "Full", "Wait 20 mins"]
            ], columns=["Station", "Distance", "Charger Type", "Availability", "Status"])

            st.dataframe(ev_data, use_container_width=True)
            st.success("AI Suggestion: Go to BESCOM EV Charging Station because it is nearest and has available slots.")
            st.caption("Slot availability is simulated for prototype demo. Real deployment can connect with EV charging APIs.")
            show_simple_map(detected_area)

        # ====================== VEHICLE SERVICE ======================
        elif intent == "Vehicle Service":
            st.subheader("🛠️ Vehicle Service Assistant")

            service_data = pd.DataFrame([
                ["Honda Authorized Service", "1.8 km", "Bike/Car Service", "Open"],
                ["QuickFix Auto Garage", "2.4 km", "General Repair", "Open"],
                ["City Motors Support", "3.0 km", "Vehicle Diagnostics", "Open"]
            ], columns=["Service Center", "Distance", "Service Type", "Status"])

            st.dataframe(service_data, use_container_width=True)
            st.info("AI Note: If you meant EV charging, search for 'EV charging near me'. If you meant Honda support, these are nearby service options.")
            show_simple_map(detected_area)

        # ====================== GENERAL CITY HELP ======================
        else:
            st.subheader("🧭 General City Help")

            st.info(f"""
I understood your query: **{user_query}**

**Detected Area:** {detected_area}

SmartCity AI can currently help with:
- 🚑 Ambulance and emergency response
- 🏥 Hospital bed discovery
- 🛣️ Traffic and route guidance
- 📢 Civic complaints
- 🔋 EV charging points
- 🛠️ Vehicle service centers
- 🗺️ Map-based city support
""")
            show_simple_map(detected_area)

# ====================== MODULE INFO PAGES ======================
if page == "🚑 Emergency":
    st.divider()
    st.subheader("🚑 Emergency Module")
    st.write("Use the chat above and type: **I need ambulance in Jayanagar**")

elif page == "🛣️ Traffic":
    st.divider()
    st.subheader("🛣️ Traffic Module")
    st.write("Use the chat above and type: **Heavy traffic near Koramangala**")

elif page == "📢 Complaints":
    st.divider()
    st.subheader("📢 Complaint Module")
    st.write("Use the chat above and type: **Pothole in Electronic City**")

# ====================== QUICK ACTIONS ======================
st.divider()
st.subheader("⚡ Quick Actions")

cols = st.columns(6)

with cols[0]:
    if st.button("🚑 Ambulance"):
        st.info("Type: I need ambulance in Whitefield")

with cols[1]:
    if st.button("🛣️ Traffic"):
        st.info("Type: Heavy traffic near Koramangala")

with cols[2]:
    if st.button("📢 Complaint"):
        st.info("Type: Pothole in Electronic City")

with cols[3]:
    if st.button("🏥 Hospital"):
        st.info("Type: Hospital beds near Jayanagar")

with cols[4]:
    if st.button("🔋 EV Charging"):
        st.info("Type: Find EV charging points near me")

with cols[5]:
    if st.button("🛠️ Service"):
        st.info("Type: Honda service center near me")

st.caption("ByteForge_SmartCityAI • Testing Version | Multi-Agent Ready")