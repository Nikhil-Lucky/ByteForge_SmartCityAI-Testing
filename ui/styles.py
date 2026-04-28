"""
Custom CSS Styles for SmartCity AI
Author: Sunay (Team ByteForge)

Premium dark theme with glassmorphism, gradients, and micro-animations.
"""


def get_custom_css():
    """Return the full custom CSS for the SmartCity AI app."""
    return """
    <style>
    /* ============================================
       GOOGLE FONTS
       ============================================ */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    /* ============================================
       ROOT VARIABLES / DESIGN TOKENS
       ============================================ */
    :root {
        --bg-primary: #0a0e1a;
        --bg-secondary: #111827;
        --bg-card: rgba(17, 24, 39, 0.7);
        --bg-glass: rgba(255, 255, 255, 0.03);
        --border-glass: rgba(255, 255, 255, 0.08);
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --accent-blue: #3b82f6;
        --accent-cyan: #06b6d4;
        --accent-emerald: #10b981;
        --accent-amber: #f59e0b;
        --accent-red: #ef4444;
        --accent-purple: #8b5cf6;
        --gradient-primary: linear-gradient(135deg, #3b82f6, #06b6d4);
        --gradient-danger: linear-gradient(135deg, #ef4444, #f97316);
        --gradient-success: linear-gradient(135deg, #10b981, #06b6d4);
        --gradient-purple: linear-gradient(135deg, #8b5cf6, #ec4899);
        --shadow-glow: 0 0 20px rgba(59, 130, 246, 0.15);
        --shadow-card: 0 4px 24px rgba(0, 0, 0, 0.3);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 20px;
        --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        --transition-smooth: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ============================================
       GLOBAL / BODY OVERRIDES
       ============================================ */
    .stApp {
        background: var(--bg-primary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: var(--text-primary) !important;
    }

    .stApp > header {
        background: transparent !important;
    }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px !important;
    }

    /* ============================================
       SIDEBAR STYLING
       ============================================ */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%) !important;
        border-right: 1px solid var(--border-glass) !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem !important;
    }

    section[data-testid="stSidebar"] [data-testid="stMarkdown"] p {
        color: var(--text-secondary) !important;
    }

    section[data-testid="stSidebar"] .stRadio > label {
        color: var(--text-primary) !important;
        font-weight: 500 !important;
    }

    section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label {
        background: var(--bg-glass) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.7rem 1rem !important;
        margin-bottom: 0.35rem !important;
        transition: all var(--transition-smooth) !important;
        cursor: pointer !important;
    }

    section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:hover {
        background: rgba(59, 130, 246, 0.1) !important;
        border-color: rgba(59, 130, 246, 0.3) !important;
        transform: translateX(4px);
    }

    section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label[data-checked="true"],
    section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label[aria-checked="true"] {
        background: rgba(59, 130, 246, 0.15) !important;
        border-color: var(--accent-blue) !important;
        box-shadow: 0 0 12px rgba(59, 130, 246, 0.2) !important;
    }

    /* ============================================
       HEADINGS & TYPOGRAPHY
       ============================================ */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        color: var(--text-primary) !important;
    }

    h1 {
        font-weight: 800 !important;
        letter-spacing: -0.02em !important;
    }

    /* ============================================
       BUTTONS
       ============================================ */
    .stButton > button {
        background: var(--gradient-primary) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-md) !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: 0.01em !important;
        transition: all var(--transition-smooth) !important;
        box-shadow: 0 4px 14px rgba(59, 130, 246, 0.25) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important;
        filter: brightness(1.1) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ============================================
       TEXT INPUTS
       ============================================ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        transition: border-color var(--transition-fast) !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent-blue) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
    }

    /* ============================================
       METRIC CARDS
       ============================================ */
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-lg) !important;
        padding: 1.2rem !important;
        backdrop-filter: blur(10px) !important;
        transition: all var(--transition-smooth) !important;
    }

    [data-testid="stMetric"]:hover {
        border-color: rgba(59, 130, 246, 0.3) !important;
        box-shadow: var(--shadow-glow) !important;
        transform: translateY(-2px) !important;
    }

    [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }

    [data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        font-size: 1.5rem !important;
    }

    /* ============================================
       ALERT BOXES
       ============================================ */
    .stAlert {
        border-radius: var(--radius-md) !important;
        border: 1px solid var(--border-glass) !important;
        backdrop-filter: blur(8px) !important;
    }

    /* ============================================
       TABS
       ============================================ */
    .stTabs [data-baseweb="tab-list"] {
        background: var(--bg-secondary) !important;
        border-radius: var(--radius-lg) !important;
        padding: 4px !important;
        gap: 4px !important;
        border: 1px solid var(--border-glass) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-md) !important;
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 0.5rem 1rem !important;
        transition: all var(--transition-fast) !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-primary) !important;
        background: rgba(59, 130, 246, 0.1) !important;
    }

    .stTabs [aria-selected="true"] {
        background: var(--gradient-primary) !important;
        color: white !important;
    }

    /* ============================================
       EXPANDER
       ============================================ */
    .streamlit-expanderHeader {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        font-weight: 500 !important;
    }

    /* ============================================
       DIVIDER
       ============================================ */
    hr {
        border-color: var(--border-glass) !important;
        margin: 1.5rem 0 !important;
    }

    /* ============================================
       CUSTOM CARD COMPONENT
       ============================================ */
    .smart-card {
        background: var(--bg-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-xl);
        padding: 1.5rem;
        backdrop-filter: blur(12px);
        transition: all var(--transition-smooth);
        margin-bottom: 1rem;
    }

    .smart-card:hover {
        border-color: rgba(59, 130, 246, 0.3);
        box-shadow: var(--shadow-glow);
        transform: translateY(-2px);
    }

    .smart-card .card-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.8rem;
    }

    .smart-card .card-icon {
        font-size: 1.8rem;
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: var(--radius-md);
        background: rgba(59, 130, 246, 0.1);
    }

    .smart-card .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-primary);
    }

    .smart-card .card-subtitle {
        font-size: 0.8rem;
        color: var(--text-muted);
    }

    .smart-card .card-body {
        color: var(--text-secondary);
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* ============================================
       STATUS BADGE
       ============================================ */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 100px;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .status-badge.online {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .status-badge.busy {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }

    .status-badge.warning {
        background: rgba(245, 158, 11, 0.15);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }

    /* ============================================
       HERO BANNER
       ============================================ */
    .hero-banner {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
        border: 1px solid rgba(59, 130, 246, 0.15);
        border-radius: var(--radius-xl);
        padding: 2.5rem;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .hero-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 50%, rgba(59, 130, 246, 0.05), transparent 50%),
                    radial-gradient(circle at 70% 50%, rgba(139, 92, 246, 0.05), transparent 50%);
        animation: heroPulse 8s ease-in-out infinite;
    }

    @keyframes heroPulse {
        0%, 100% { transform: scale(1) rotate(0deg); }
        50% { transform: scale(1.05) rotate(2deg); }
    }

    .hero-banner h1 {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #60a5fa, #a78bfa, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
    }

    .hero-banner p {
        color: var(--text-secondary);
        font-size: 1.05rem;
        max-width: 600px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }

    /* ============================================
       FEATURE GRID
       ============================================ */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }

    .feature-item {
        background: var(--bg-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 1.3rem;
        transition: all var(--transition-smooth);
        cursor: default;
    }

    .feature-item:hover {
        border-color: rgba(59, 130, 246, 0.3);
        transform: translateY(-3px);
        box-shadow: var(--shadow-glow);
    }

    .feature-item .feat-icon { font-size: 2rem; margin-bottom: 0.5rem; }
    .feature-item .feat-title { font-weight: 600; color: var(--text-primary); margin-bottom: 0.3rem; }
    .feature-item .feat-desc { font-size: 0.85rem; color: var(--text-muted); line-height: 1.5; }

    /* ============================================
       SCROLLBAR
       ============================================ */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-primary); }
    ::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.2); border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(148, 163, 184, 0.4); }

    /* ============================================
       PULSE DOT
       ============================================ */
    .pulse-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--accent-emerald);
        animation: pulse-anim 1.5s ease-in-out infinite;
        margin-right: 6px;
    }

    @keyframes pulse-anim {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(0.8); }
    }

    /* ============================================
       FOOTER
       ============================================ */
    .app-footer {
        text-align: center;
        padding: 1.5rem 0;
        color: var(--text-muted);
        font-size: 0.8rem;
        border-top: 1px solid var(--border-glass);
        margin-top: 2rem;
    }

    .app-footer a { color: var(--accent-blue); text-decoration: none; }
    .app-footer a:hover { text-decoration: underline; }

    /* ============================================
       RESPONSIVE
       ============================================ */
    @media (max-width: 768px) {
        .hero-banner h1 { font-size: 1.5rem; }
        .hero-banner { padding: 1.5rem; }
        .feature-grid { grid-template-columns: 1fr; }
    }
    </style>
    """


def render_smart_card(icon, title, subtitle, body):
    """Return HTML for a glassmorphism card component."""
    return f'<div class="smart-card"><div class="card-header"><div class="card-icon">{icon}</div><div><div class="card-title">{title}</div><div class="card-subtitle">{subtitle}</div></div></div><div class="card-body">{body}</div></div>'


def render_status_badge(text, status="online"):
    """Return HTML for a status badge. status: online | busy | warning"""
    return f'<span class="status-badge {status}">● {text}</span>'


def render_hero_banner(title, subtitle):
    """Return HTML for the hero banner on the home page."""
    return f'<div class="hero-banner"><h1>{title}</h1><p>{subtitle}</p></div>'


def render_feature_grid(features):
    """Render a CSS grid of feature cards."""
    items = ""
    for f in features:
        items += f'<div class="feature-item"><div class="feat-icon">{f["icon"]}</div><div class="feat-title">{f["title"]}</div><div class="feat-desc">{f["desc"]}</div></div>'
    return f'<div class="feature-grid">{items}</div>'
