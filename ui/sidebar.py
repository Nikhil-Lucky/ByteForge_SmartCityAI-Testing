"""
Sidebar Component for SmartCity AI
Author: Sunay (Team ByteForge)

Renders the branded sidebar with navigation, city stats, and system info.
"""

import streamlit as st
from datetime import datetime
from ui.styles import render_status_badge


# Navigation page definitions
NAV_PAGES = [
    {"label": "🏠 Dashboard", "key": "dashboard"},
    {"label": "🚑 Emergency Services", "key": "emergency"},
    {"label": "🛣️ Traffic & Routes", "key": "traffic"},
    {"label": "📢 Civic Complaints", "key": "complaints"},
    {"label": "🗺️ Live City Map", "key": "live_map"},
    {"label": "💬 AI Chat Assistant", "key": "chat"},
]


def render_sidebar():
    """Render the full sidebar and return the selected page key."""
    with st.sidebar:
        # ── Branding ──
        st.markdown("""
        <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
            <div style="font-size: 2.8rem; margin-bottom: 0.2rem;">🏙️</div>
            <div style="
                font-size: 1.4rem;
                font-weight: 800;
                background: linear-gradient(135deg, #60a5fa, #a78bfa);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                letter-spacing: -0.02em;
            ">SmartCity AI</div>
            <div style="
                font-size: 0.75rem;
                color: #64748b;
                margin-top: 2px;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            ">Bengaluru • Real-Time Intelligence</div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── System Status ──
        st.markdown(
            f'<div style="display:flex; align-items:center; gap:8px; margin-bottom:0.5rem;">'
            f'{render_status_badge("System Online", "online")}'
            f'</div>',
            unsafe_allow_html=True
        )

        current_time = datetime.now().strftime("%I:%M %p • %d %b %Y")
        st.caption(f"🕐 {current_time}")

        st.divider()

        # ── Navigation ──
        st.markdown("""
        <div style="
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #64748b;
            font-weight: 600;
            margin-bottom: 0.5rem;
            padding-left: 0.2rem;
        ">Navigation</div>
        """, unsafe_allow_html=True)

        page_labels = [p["label"] for p in NAV_PAGES]
        selected_label = st.radio(
            "Navigate",
            page_labels,
            label_visibility="collapsed",
            key="nav_radio"
        )

        # Map label back to key
        selected_key = "dashboard"
        for p in NAV_PAGES:
            if p["label"] == selected_label:
                selected_key = p["key"]
                break

        st.divider()

        # ── Quick City Stats ──
        st.markdown("""
        <div style="
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #64748b;
            font-weight: 600;
            margin-bottom: 0.5rem;
            padding-left: 0.2rem;
        ">Live City Pulse</div>
        """, unsafe_allow_html=True)

        stat_col1, stat_col2 = st.columns(2)
        with stat_col1:
            st.metric("🚑 Ambulances", "3 Free", delta="1 dispatched")
        with stat_col2:
            st.metric("🚦 Traffic", "Medium", delta="-12%")

        stat_col3, stat_col4 = st.columns(2)
        with stat_col3:
            st.metric("📢 Open Issues", "27", delta="3 new")
        with stat_col4:
            st.metric("🌤️ Weather", "29°C", delta="Partly Cloudy")

        st.divider()

        # ── Team Info ──
        st.markdown("""
        <div style="
            text-align: center; 
            padding: 0.8rem;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 12px;
        ">
            <div style="font-size:0.85rem; font-weight:600; color:#94a3b8;">Team ByteForge</div>
            <div style="font-size:0.7rem; color:#64748b; margin-top:4px;">
                Nikhil • Sunay • Suhas • Shahid
            </div>
            <div style="font-size:0.65rem; color:#475569; margin-top:6px;">
                Hackathon 2026 • TECH_FUSION
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.caption("Made with ❤️ for Bengaluru")

    return selected_key
