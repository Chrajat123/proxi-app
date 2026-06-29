import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta

# 1. Premium Page Configuration
st.set_page_config(page_title="Proxi | Execution AI", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# 2. Ultra-Modern "Cyber-Neon" CSS Styling
st.markdown("""
    <style>
    /* Global Theme - Deep Dark Blue/Black */
    .stApp { background-color: #0b0e14; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Sleek Typography */
    h1, h2, h3 { color: #ffffff; font-weight: 800; letter-spacing: -0.5px; }
    
    /* Premium Metric Cards */
    .metric-card { 
        background: #151a25;
        border: 1px solid #2a3441; 
        padding: 20px; 
        border-radius: 16px; 
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease;
    }
    .metric-card:hover { transform: translateY(-5px); border-color: #00f2fe; }
    
    /* Task Cards */
    .task-card { 
        background-color: #151a25; 
        border: 1px solid #2a3441; 
        padding: 24px; 
        border-radius: 12px; 
        margin-bottom: 16px; 
        transition: all 0.3s ease;
    }
    .task-card:hover { 
        transform: translateY(-3px); 
        border-color: #f12711; 
        box-shadow: 0 8px 30px rgba(241, 39, 17, 0.2); 
    }
    
    /* Priority Indicators - Brighter Neon Colors */
    .priority-indicator { padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
    .bg-critical { background: #ff0844; color: #ffffff; box-shadow: 0 0 10px rgba(255, 8, 68, 0.5); }
    .bg-high { background: #f59e0b; color: #ffffff; box-shadow: 0 0 10px rgba(245, 158, 11, 0.5); }
    .bg-med { background: #00f2fe; color: #1a1a1a; box-shadow: 0 0 10px rgba(0, 242, 254, 0.5); }
    .bg-low { background: #10b981; color: #ffffff; box-shadow: 0 0 10px rgba(16, 185, 129, 0.5); }
    
    /* =========================================
       🔥 THE FIX: BRIGHT ACTIVE TABS & BUTTONS 
       ========================================= */
       
    /* 1. Style the Tabs (Action Feed, Input, Archive) */
    button[data-baseweb="tab"] {
        background-color: #1a2333 !important;
        border-radius: 8px 8px 0px 0px !important;
        color: #7d8da6 !important;
        padding: 12px 24px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: none !important;
        margin-right: 5px !important;
        transition: all 0.3s ease !important;
    }
    
    /* 2. Style the ACTIVE Tab (Bright Gradient & Glow) */
    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #00f2fe, #4facfe) !important;
        color: #ffffff !important;
        box-shadow: 0 -4px 20px rgba(0, 242, 254, 0.5) !important;
    }
    
    button[data-baseweb="tab"]:hover {
        color: #ffffff !important;
        background-color: #2a3441 !important;
    }

    /* 3. Global Action Buttons (Submit, Complete) */
    .stButton>button { 
        background: linear-gradient(90deg, #f12711, #f5af19) !important; 
        color: white !important; 
        border: none !important; 
        border-radius: 8px !important; 
        font-weight: 800 !important; 
        font-size: 16px !important;
        padding: 0.6rem 1.2rem !important; 
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(241, 39, 17, 0.4) !important;
    }
    .stButton>button:hover { 
        transform: scale(1.02) !important;
        box-shadow: 0 6px 20px rgba(241, 39, 17, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Session State Initialization
if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"task": "Finalize Capstone Project Report", "deadline": date.today() + timedelta(days=2), "importance": "Critical", "effort": 6, "done": False},
        {"task": "Prepare Investor Pitch Deck", "deadline": date.today() + timedelta(days=5), "importance": "High", "effort": 4, "done": False},
        {"task": "Update LinkedIn Profile", "deadline": date.today() + timedelta(days=14), "importance": "Low", "effort": 1, "done": False},
        {"task": "Pay Monthly Internet Bill", "deadline": date.today() - timedelta(days=1), "importance": "Medium", "effort": 1, "done": True}
    ]

# 4. App Header (Minimalist)
st.markdown("<h1>⚡ Proxi <span style='color:#00f2fe; font-weight:400; font-size: 24px;'>// Proactive Execution Engine</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#7d8da6; font-size:18px;'>Stop missing deadlines. Let AI orchestrate your priorities.</p>", unsafe_allow_html=True)
st.write("---")

# 5. Dashboard Metrics (KPIs)
tasks_total = len(st.session_state.tasks)
tasks_done = len([t for t in st.session_state.tasks if t['done']])
tasks_active = tasks_total - tasks_done
completion_rate = int((tasks_done / tasks_total * 100)) if tasks_total > 0 else 0

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.markdown(f"<div class='metric-card'><h2 style='color:#00f2fe; margin:0;'>{tasks_active}</h2><p style='color:#7d8da6; margin:0;'>Active Missions</p></div>", unsafe_allow_html=True)
with col_m2:
    st.markdown(f"<div class='metric-card'><h2 style='color:#10b981; margin:0;'>{tasks_done}</h2><p style='color:#7d8da6; margin:0;'>Missions Accomplished</p></div>", unsafe_allow_html=True)
with col_m3:
    st.markdown(f"<div class='metric-card'><h2 style='color:#f59e0b; margin:0;'>{completion_rate}%</h2><p style='color:#7d8da6; margin:0;'>Execution Rate</p></div>", unsafe_allow_html=True)
with col_m4:
    st.markdown(f"<div class='metric-card'><h2 style='color:#ff0844; margin:0;'>Live</h2><p style='color:#7d8da6; margin:0;'>AI Status</p></div>", unsafe_allow_html=True)

st.write("")
st.progress(completion_rate / 100, text=f"Overall Completion: {completion_rate}%")
st.write("")

# 6. Modern Tabbed Interface
tab1, tab2, tab3 = st.tabs(["🎯 Action Feed", "📥 Input New Data", "🗄️ Execution Archive"])

# TAB 1: AI ACTION FEED
with tab1:
    active_tasks = [t for i, t in enumerate(st.session_state.tasks) if not t['done']]
    
    if not active_tasks:
        st.success("You are at Inbox Zero! Incredible execution.")
    else:
        processed_tasks = []
        for t in active_tasks:
            days_left = (t['deadline'] - date.today()).days
            safe_days = max(days_left, 0.1) # Prevent zero division
            
            # AI Weighting
            weights = {"Low": 1, "Medium": 2, "High": 3, "Critical": 5}
            urgency_multiplier = (1 / safe_days) * 20 if safe_days > 0 else 50
            score = round((weights[t['importance']] * 10) + (t['effort'] * 2) + urgency_multiplier, 1)
            
            # Determine color tag
            tag_class = "bg-low"
            if t['importance'] == "Critical": tag_class = "bg-critical"
            elif t['importance'] == "High": tag_class = "bg-high"
            elif t['importance'] == "Medium": tag_class = "bg-med"
            
            processed_tasks.append({**t, "score": score, "days": days_left, "tag": tag_class})
            
        # Sort by AI Score
        processed_tasks = sorted(processed_tasks, key=lambda x: x['score'], reverse=True)
        
        st.markdown("### 🔥 High-Priority Interventions")
        
        for idx, pt in enumerate(processed_tasks):
            time_warning = f"<span style='color:#ff0844; font-weight:bold;'>⚠️ LATE ({abs(pt['days'])} days)</span>" if pt['days'] < 0 else f"⏱️ {pt['days']} Days Remaining"
            
            st.markdown(f"""
                <div class='task-card'>
                    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'>
                        <h3 style='margin: 0;'>{pt['task']}</h3>
                        <span class='priority-indicator {pt['tag']}'>{pt['importance']}</span>
                    </div>
                    <p style='color: #7d8da6; margin-bottom: 15px; font-size: 14px;'>
                        {time_warning} &nbsp;|&nbsp; 🔋 Effort: {pt['effort']} hrs &nbsp;|&nbsp; 🧠 <b>Proxi Score: {pt['score']}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("↳ View Proxi Breakdown & Execute"):
                st.write(f"**Step 1:** Block {round(pt['effort']/3, 1)} hours immediately to establish the baseline.")
                st.write("**Step 2:** Deep work session activated. Eliminate distractions.")
                
                # We need the original index to update the main list
                original_index = st.session_state.tasks.index(next(item for item in st.session_state.tasks if item["task"] == pt['task']))
                
                if st.button(f"Mark Accomplished", key=f"done_{idx}"):
                    st.session_state.tasks[original_index]['done'] = True
                    st.rerun()

# TAB 2: ADD NEW TASKS
with tab2:
    st.markdown("### 📥 Inject Task into Neural Queue")
    with st.container(border=True):
        with st.form("new_task_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                new_task = st.text_input("Objective Name", placeholder="e.g., Code Review for Sprint 4")
                new_deadline = st.date_input("Hard Deadline", min_value=date.today())
            with col2:
                new_importance = st.selectbox("Strategic Value", ["Low", "Medium", "High", "Critical"])
                new_effort = st.slider("Estimated Time Cost (Hours)", 1, 20, 2)
                
            submit_task = st.form_submit_button("Engage Proxi AI")
            
            if submit_task and new_task:
                st.session_state.tasks.append({
                    "task": new_task, "deadline": new_deadline, "importance": new_importance, "effort": new_effort, "done": False
                })
                st.success("Target acquired. Proxi has recalculated your priorities.")
                st.rerun()

# TAB 3: ARCHIVE
with tab3:
    st.markdown("### 🗄️ Mission Archive")
    archived = [t for t in st.session_state.tasks if t['done']]
    
    if not archived:
        st.caption("No missions accomplished yet. Time to get to work.")
    else:
        for t in archived:
            st.markdown(f"""
            <div style='padding: 15px; border-bottom: 1px solid #2a3441; color: #7d8da6;'>
                <s><b>{t['task']}</b></s> — Completed
            </div>
            """, unsafe_allow_html=True)
