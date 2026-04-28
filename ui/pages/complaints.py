"""
Civic Complaints Page
Author: Sunay (Team ByteForge)
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from ui.styles import render_smart_card, render_status_badge

MOCK_COMPLAINTS = [
    {"id": "COMP-1401", "type": "Pothole", "area": "Jayanagar 7th Block", "status": "In Progress", "date": "28 Apr 2026", "priority": "High"},
    {"id": "COMP-1398", "type": "Garbage", "area": "Jayanagar 4th Block", "status": "Submitted", "date": "27 Apr 2026", "priority": "Medium"},
    {"id": "COMP-1395", "type": "Street Light", "area": "Jayanagar 3rd Block", "status": "Resolved", "date": "26 Apr 2026", "priority": "Low"},
    {"id": "COMP-1390", "type": "Water Supply", "area": "Jayanagar 5th Block", "status": "In Progress", "date": "25 Apr 2026", "priority": "High"},
    {"id": "COMP-1385", "type": "Power Cut", "area": "Jayanagar 9th Block", "status": "Submitted", "date": "25 Apr 2026", "priority": "Medium"},
]

COMPLAINT_CATEGORIES = ["🕳️ Pothole / Road Damage", "🗑️ Garbage / Waste", "💧 Water Supply", "⚡ Power Cut / Electrical", "💡 Street Light", "🚰 Drainage / Sewage", "🌳 Tree Fall", "🔇 Noise Pollution", "🚧 Illegal Construction", "📋 Other"]


def render_complaints_page():
    st.markdown('<div style="display:flex; align-items:center; gap:12px; margin-bottom:0.5rem;"><div style="font-size:2.2rem; width:56px; height:56px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg, rgba(139,92,246,0.15), rgba(236,72,153,0.15)); border-radius:16px; border:1px solid rgba(139,92,246,0.2);">📢</div><div><div style="font-size:1.5rem; font-weight:700; color:#f1f5f9;">Civic Complaint Manager</div><div style="font-size:0.85rem; color:#94a3b8;">Register, track & resolve civic issues with AI categorization</div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    comp_tabs = st.tabs(["📝 Register Complaint", "📋 My Complaints", "📊 Area Analysis"])

    with comp_tabs[0]:
        st.markdown("### 📝 Register a New Complaint")
        with st.form("complaint_form", clear_on_submit=True):
            fc1, fc2 = st.columns(2)
            with fc1:
                category = st.selectbox("📂 Category", COMPLAINT_CATEGORIES, key="comp_cat")
            with fc2:
                area = st.text_input("📍 Location / Area", placeholder="e.g., Jayanagar 7th Block", key="comp_area")
            description = st.text_area("📝 Describe the issue", placeholder="Large pothole near bus stop on 11th Main Road...", height=120, key="comp_desc")
            fc3, fc4 = st.columns(2)
            with fc3:
                severity = st.select_slider("⚠️ Severity", options=["Low", "Medium", "High", "Critical"], value="Medium", key="comp_severity")
            with fc4:
                contact = st.text_input("📱 Contact (optional)", placeholder="Phone or email", key="comp_contact")
            submitted = st.form_submit_button("🚀 Submit Complaint", use_container_width=True)
            if submitted:
                if not area or not description:
                    st.error("⚠️ Please provide location and description.")
                else:
                    comp_id = f"COMP-{datetime.now().strftime('%H%M%S')}"
                    st.success(f"✅ **Complaint Registered!**")
                    st.markdown(render_smart_card("📋", f"Complaint {comp_id}", f"Registered at {datetime.now().strftime('%I:%M %p')}",
                        f'<div>📂 <strong>Category:</strong> {category}</div><div>📍 <strong>Area:</strong> {area}</div><div>⚠️ <strong>Severity:</strong> {severity}</div><div>⏳ <strong>Resolution:</strong> 48 hours</div><div style="margin-top:0.5rem;">{render_status_badge("Submitted", "online")}</div>'
                    ), unsafe_allow_html=True)
                    st.info("💡 **AI-categorized and prioritized** based on severity and similar reports.")

    with comp_tabs[1]:
        st.markdown("### 📋 Complaint Tracker")
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            status_filter = st.selectbox("Filter by Status", ["All", "Submitted", "In Progress", "Resolved"], key="comp_filter")
        with filter_col2:
            sort_by = st.selectbox("Sort by", ["Newest First", "Priority", "Status"], key="comp_sort")

        status_map = {"Submitted": "warning", "In Progress": "online", "Resolved": "online"}
        priority_map = {"High": "busy", "Medium": "warning", "Low": "online"}

        for comp in MOCK_COMPLAINTS:
            if status_filter != "All" and comp["status"] != status_filter:
                continue
            st.markdown(render_smart_card("📋", f"{comp['id']} — {comp['type']}", f"{comp['area']} • {comp['date']}",
                f'<div style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:0.5rem;"><div>Status: {render_status_badge(comp["status"], status_map.get(comp["status"], "warning"))}</div><div>Priority: {render_status_badge(comp["priority"], priority_map.get(comp["priority"], "warning"))}</div></div>'
            ), unsafe_allow_html=True)

    with comp_tabs[2]:
        st.markdown("### 📊 Complaint Analysis — Jayanagar Area")
        an_col1, an_col2, an_col3, an_col4 = st.columns(4)
        with an_col1:
            st.metric("Total Complaints", "27", delta="3 this week")
        with an_col2:
            st.metric("Resolved", "18", delta="67% rate")
        with an_col3:
            st.metric("In Progress", "6")
        with an_col4:
            st.metric("Pending", "3", delta="2 overdue", delta_color="inverse")

        st.divider()
        st.markdown("#### 📂 Complaints by Category")
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            chart_data = pd.DataFrame({"Category": ["Pothole", "Garbage", "Water", "Street Light", "Power", "Drainage"], "Count": [8, 6, 5, 4, 3, 1]})
            st.bar_chart(chart_data.set_index("Category"), color="#3b82f6")
        with chart_col2:
            st.markdown(render_smart_card("💡", "AI Insights", "Pattern Analysis",
                '<div style="line-height:1.8;"><div>🔴 <strong>Potholes</strong> are #1 issue (30%)</div><div>📍 <strong>7th Block</strong> has highest density</div><div>📈 Garbage complaints <strong>up 40%</strong></div><div>✅ Street lights have <strong>fastest resolution</strong> (24 hrs)</div><div>⚠️ Water complaints <strong>peak on weekends</strong></div></div>'
            ), unsafe_allow_html=True)
