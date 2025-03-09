import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Learning Tracker", layout="wide")


st.sidebar.title("Learning Tracker")

if "menu" not in st.session_state:
    st.session_state["menu"] = "Home"

menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Set Goals", "Daily Log", "Progress Dashboard", "Motivation"],
    index=["Home", "Set Goals", "Daily Log", "Progress Dashboard", "Motivation"].index(st.session_state["menu"])
)

if "goals" not in st.session_state:
    st.session_state["goals"] = []
if "logs" not in st.session_state:
    st.session_state["logs"] = []



if menu == "Home":
    st.markdown("""
        <style>
        .hero-text {
            font-size: 3em;
            color: #2E8B57;
            text-align: center;
            margin-top: 20px;
        }
        .subtext {
            font-size: 1.2em;
            text-align: center;
            color: #555;
            margin-bottom: 20px;
        }
        .features {
            background-color: #F0F8FF;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .feature-item {
            font-size: 1.1em;
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="hero-text">🚀 Welcome to the Learning Tracker!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Track your learning journey, adopt a growth mindset, and achieve your goals!</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🌟 Key Features:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Set Goals")
        st.write("Define your learning objectives and maintain focus.")

    with col2:
        st.markdown("### 📈 Track Progress")
        st.write("Log daily learning activities and visualize your growth.")

    with col3:
        st.markdown("### 💪 Stay Motivated")
        st.write("Receive motivational content to keep pushing forward.")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    st.markdown("### 💡 Motivation for You:")
    st.success("“Success is not an accident, success is a choice.” – Stephen Curry")

    st.markdown("<div style='text-align: center; margin-top: 30px;'>", unsafe_allow_html=True)
    
    if st.button("Get Started Now!"):
        st.session_state["menu"] = "Set Goals"
        st.experimental_rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)



# Goal Setting Page

elif menu == "Set Goals":
    st.header("Set Your Learning Goals")
    goal = st.text_input("Learning Goal", placeholder="e.g., Learn Python Basics")
    
    if st.button("Add Goal"):
        if goal:
            st.session_state["goals"].append({"goal": goal, "completed": False})
            st.success("Goal added!")

    if st.session_state["goals"]:
        st.subheader("Your Goals")
        for i, g in enumerate(st.session_state["goals"]):
            col1, col2 = st.columns([8, 2])
            goal_text = f"✅ {g['goal']}" if g["completed"] else g["goal"]
            col1.write(goal_text)
            if not g["completed"] and col2.button("Complete", key=f"complete_{i}"):
                st.session_state["goals"][i]["completed"] = True
                st.experimental_rerun()



# Daily Log Page

elif menu == "Daily Log":
    st.header("Daily Learning Log")
    date = st.date_input("Date")
    activity = st.text_area("What did you learn today?", placeholder="Describe your learning experience")
    duration = st.number_input("Time Spent (in minutes)", min_value=0, max_value=1440, step=10)
    
    if st.button("Save Log"):
        if activity and duration > 0:
            st.session_state["logs"].append({"date": date, "activity": activity, "duration": duration})
            st.success("Log saved!")


# Progress Dashboard

elif menu == "Progress Dashboard":
    st.header("Your Learning Progress")

    if st.session_state["logs"]:
        df = pd.DataFrame(st.session_state["logs"])
        
        st.write("### Learning Logs")
        st.dataframe(df)

        st.write("### Learning Duration Over Time")
        fig = px.line(df, x="date", y="duration", title="Learning Duration Over Time", markers=True)
        st.plotly_chart(fig)

        st.write("### Learning Activity Distribution")
        fig2 = px.bar(df, x="date", y="duration", color="activity", title="Activities and Time Spent")
        st.plotly_chart(fig2)
    else:
        st.info("No logs available. Please add your learning logs to see progress.")


# Motivation Section

elif menu == "Motivation":
    st.header("Stay Motivated!")
    st.write("Here's a motivational quote to keep you going:")
    st.info("“The best way to predict your future is to create it.” – Abraham Lincoln")

    st.write("### 📽️ Watch This!")
    st.video("https://www.youtube.com/watch?v=ZXsQAXx_ao0")