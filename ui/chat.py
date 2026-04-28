"""
Chat Interface Component for SmartCity AI
Author: Sunay (Team ByteForge)

Full chat UI with session-state message history, quick actions,
and styled message bubbles. Ready for Nikhil's multi-agent backend.
"""

import streamlit as st
from datetime import datetime


def init_chat_state():
    """Initialize chat-related session state variables."""
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 Hello! I'm **SmartCity AI**, your intelligent assistant for Bengaluru.\n\n"
                    "I can help you with:\n"
                    "- 🚑 **Emergency services** — Find nearest ambulance & hospital\n"
                    "- 🛣️ **Traffic & routes** — Best route suggestions\n"
                    "- 📢 **Civic complaints** — Report & track issues\n"
                    "- 🗺️ **Live city data** — Maps, weather, resources\n\n"
                    "Try asking: *\"I need an ambulance in Jayanagar 3rd Block\"*"
                ),
                "timestamp": datetime.now().strftime("%I:%M %p"),
            }
        ]


def get_ai_response(user_message):
    """
    Generate an AI response for the user's message.
    NOTE: This is a placeholder. Nikhil will replace with multi-agent pipeline.
    """
    msg_lower = user_message.lower()

    if any(kw in msg_lower for kw in ["ambulance", "emergency", "accident", "hospital", "hurt", "help"]):
        return (
            "🚨 **Emergency Detected!**\n\n"
            "I've activated the emergency response system:\n\n"
            "| Detail | Info |\n|---|---|\n"
            "| 🚑 Nearest Ambulance | **AMB001** — Jayanagar General |\n"
            "| ⏱️ Estimated ETA | **9 minutes** |\n"
            "| 🏥 Recommended Hospital | **Jayanagar General Hospital** |\n"
            "| 🛏️ Beds Available | **12** |\n\n"
            "📍 Ambulance has been dispatched and is en route.\n\n"
            "💡 *Why this recommendation?* AMB001 is the closest free unit with the shortest ETA. "
            "Jayanagar General has the most available beds in the area."
        )

    elif any(kw in msg_lower for kw in ["traffic", "route", "road", "jam", "majestic", "commute"]):
        return (
            "🛣️ **Smart Route Analysis**\n\n"
            "**🟢 Recommended Route:** via 100 Feet Road → Bannerghatta Road\n"
            "- ⏱️ **Est. Time:** 28 minutes\n"
            "- 🚦 **Traffic Level:** Medium\n\n"
            "**🟡 Alternate Route:** via Hosur Road → Ring Road\n"
            "- ⏱️ **Est. Time:** 35 minutes\n"
            "- 🚦 **Traffic Level:** Heavy near Silk Board\n\n"
            "💡 *Why?* Primary route has 25% less congestion and no waterlogging."
        )

    elif any(kw in msg_lower for kw in ["pothole", "garbage", "water", "complaint", "broken", "light", "power"]):
        comp_id = f"COMP-{datetime.now().strftime('%H%M%S')}"
        return (
            f"📢 **Civic Complaint Registered**\n\n"
            f"| Detail | Info |\n|---|---|\n"
            f"| 🔖 Complaint ID | **{comp_id}** |\n"
            f"| 📍 Area | **Jayanagar** (auto-detected) |\n"
            f"| ⏳ Expected Resolution | **48 hours** |\n"
            f"| 🔔 Status | **Submitted** |\n\n"
            f"We found **3 similar complaints** in your area.\n\n"
            f"💡 *Your complaint has been prioritized based on frequency in this zone.*"
        )

    elif any(kw in msg_lower for kw in ["weather", "rain", "temperature"]):
        return (
            "🌤️ **Bengaluru Weather — Live**\n\n"
            "| Parameter | Value |\n|---|---|\n"
            "| 🌡️ Temperature | **29°C** |\n"
            "| 💧 Humidity | **62%** |\n"
            "| 🌧️ Rain Probability | **15%** |\n"
            "| 💨 Wind | **12 km/h NE** |\n\n"
            "**No weather warnings** active."
        )

    else:
        return (
            f"🤖 I understand: **\"{user_message}\"**\n\n"
            "Processing via multi-agent system:\n"
            "1. 📊 **Data Agent** — Fetching real-time data\n"
            "2. 🔍 **Analysis Agent** — Processing patterns\n"
            "3. ⚡ **Optimization Agent** — Finding best action\n"
            "4. 💬 **Explanation Agent** — Preparing response\n\n"
            "🔄 *Full multi-agent pipeline being integrated by Nikhil.*\n\n"
            "Try asking about: 🚑 Ambulance | 🛣️ Traffic | 📢 Complaints | 🌤️ Weather"
        )


def render_chat_interface():
    """Render the full chat interface."""
    init_chat_state()

    st.markdown("""
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:1rem;">
        <div style="font-size:1.8rem;">💬</div>
        <div>
            <div style="font-size:1.3rem; font-weight:700; color:#f1f5f9;">SmartCity AI Assistant</div>
            <div style="font-size:0.8rem; color:#64748b;">
                <span class="pulse-dot"></span> Powered by Multi-Agent Intelligence
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Chat message history ──
    chat_container = st.container(height=450)
    with chat_container:
        for msg in st.session_state.chat_messages:
            role = msg["role"]
            avatar = "👤" if role == "user" else "🏙️"
            with st.chat_message(role, avatar=avatar):
                st.markdown(msg["content"])
                st.caption(f"🕐 {msg.get('timestamp', '')}")

    # ── Quick action buttons ──
    st.markdown("""
    <div style="font-size:0.72rem; text-transform:uppercase; letter-spacing:0.08em;
        color:#64748b; font-weight:600; margin:0.8rem 0 0.4rem 0;">Quick Actions</div>
    """, unsafe_allow_html=True)

    quick_cols = st.columns(4)
    quick_prompts = [
        ("🚑 Ambulance", "I need an ambulance in Jayanagar 3rd Block"),
        ("🛣️ Best Route", "Best route from Jayanagar to Majestic now"),
        ("📢 Pothole", "There's a pothole in Jayanagar 7th Block main road"),
        ("🌤️ Weather", "What's the weather in Bengaluru right now?"),
    ]

    for i, (label, prompt) in enumerate(quick_prompts):
        with quick_cols[i]:
            if st.button(label, key=f"quick_{i}", use_container_width=True):
                _process_message(prompt)
                st.rerun()

    # ── Chat input ──
    user_input = st.chat_input(
        "Ask SmartCity AI anything... (e.g., 'Need ambulance in Jayanagar')",
        key="chat_input_main"
    )

    if user_input:
        _process_message(user_input)
        st.rerun()


def _process_message(user_message):
    """Add user message, get AI response, and append both to history."""
    timestamp = datetime.now().strftime("%I:%M %p")

    st.session_state.chat_messages.append({
        "role": "user",
        "content": user_message,
        "timestamp": timestamp,
    })

    response = get_ai_response(user_message)

    st.session_state.chat_messages.append({
        "role": "assistant",
        "content": response,
        "timestamp": datetime.now().strftime("%I:%M %p"),
    })
