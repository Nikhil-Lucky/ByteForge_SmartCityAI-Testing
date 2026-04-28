"""
SmartCity AI — Main Application Entry Point
Author: Sunay (Team ByteForge) — UI Layer
Date: 28 April 2026

Intelligent Multi-Agent System for Real-Time Civic Decision Making
Bengaluru-focused smart city assistant built with Streamlit.

NOTE: This replaces Nikhil's basic app.py with a modular UI system.
Nikhil's router logic is preserved in ui/chat.py and will be upgraded
when the full multi-agent system is ready.
"""

import streamlit as st

# ── Page Config (MUST be first Streamlit command) ──
st.set_page_config(
    page_title="SmartCity AI — Bengaluru",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/Nikhil-Lucky/ByteForge_SmartCityAI",
        "Report a bug": "https://github.com/Nikhil-Lucky/ByteForge_SmartCityAI/issues",
        "About": "SmartCity AI — Intelligent Multi-Agent System for Real-Time Civic Decision Making. Built by Team ByteForge for Hackathon 2026."
    }
)

# ── Inject Custom CSS ──
from ui.styles import get_custom_css
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ── Render Sidebar & Get Selected Page ──
from ui.sidebar import render_sidebar
selected_page = render_sidebar()

# ── Page Router ──
if selected_page == "dashboard":
    from ui.pages.home import render_home_page
    render_home_page()

elif selected_page == "emergency":
    from ui.pages.emergency import render_emergency_page
    render_emergency_page()

elif selected_page == "traffic":
    from ui.pages.traffic import render_traffic_page
    render_traffic_page()

elif selected_page == "complaints":
    from ui.pages.complaints import render_complaints_page
    render_complaints_page()

elif selected_page == "live_map":
    from ui.pages.live_map import render_live_map_page
    render_live_map_page()

elif selected_page == "chat":
    from ui.chat import render_chat_interface
    render_chat_interface()

# ── Footer ──
st.markdown("""
<div class="app-footer">
    <div>🏙️ <strong>SmartCity AI</strong> — Intelligent Multi-Agent System for Bengaluru</div>
    <div style="margin-top:4px;">
        Built with ❤️ by <strong>Team ByteForge</strong> — 
        Nikhil • Sunay • Suhas • Shahid | 
        <a href="https://github.com/Nikhil-Lucky/ByteForge_SmartCityAI" target="_blank">GitHub</a> | 
        Hackathon 2026
    </div>
</div>
""", unsafe_allow_html=True)