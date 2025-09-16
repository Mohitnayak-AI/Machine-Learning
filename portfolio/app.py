import streamlit as st
import plotly.graph_objects as go

# ----- PAGE CONFIG -----
st.set_page_config(page_title="Mohit Nayak | Data Scientist", layout="wide")

# ----- CUSTOM CSS -----
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
        color: #e2e8f0;
    }
    .block-container {
        padding-top: 2rem;
    }
    .hero {
        text-align: center;
        padding: 3rem 0;
    }
    .hero h1 {
        font-size: 3rem;
        font-weight: 700;
        color: #06b6d4;
    }
    .hero p {
        font-size: 1.2rem;
        color: #94a3b8;
    }
    .card {
        background: rgba(30, 41, 59, 0.7);
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ----- HERO -----
st.markdown("""
<div class="hero">
    <h1>Mohit Nayak</h1>
    <p>Turning Data into Decisions with AI & Machine Learning</p>
</div>
""", unsafe_allow_html=True)

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.link_button("View My Work", "#projects")
with col2:
    st.link_button("Download CV", "https://your-cv-link.com")

# ----- ABOUT -----
st.markdown("## 👨‍💻 About Me")
col1, col2 = st.columns([1,2])
with col1:
    st.image("https://via.placeholder.com/160.png?text=Profile", width=180)
with col2:
    st.write("I am a Data Scientist with expertise in Machine Learning, Deep Learning, and MLOps. I love building end-to-end data products.")

# ----- SKILLS -----
st.markdown("## 🛠 Skills")
skills = {
    "Python": 90, "Machine Learning": 85,
    "Data Visualization": 88, "Deep Learning": 75,
    "SQL": 92, "MLOps": 70
}

skill_fig = go.Figure(go.Bar(
    x=list(skills.values()),
    y=list(skills.keys()),
    orientation='h',
    marker=dict(color='#06b6d4')
))
skill_fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(showgrid=False, visible=False),
    yaxis=dict(showgrid=False),
)
st.plotly_chart(skill_fig, use_container_width=True)

# ----- PROJECTS -----
st.markdown("## 🚀 Projects", unsafe_allow_html=True)

projects = [
    {"title": "Customer Churn Prediction Dashboard",
     "desc": "Streamlit app with ML model + insights.",
     "github": "#", "live": "#"},
    {"title": "Interactive Data Viz Case Study",
     "desc": "Plotly/D3 powered storytelling.",
     "github": "#", "live": "#"},
    {"title": "End-to-End ML Pipeline",
     "desc": "Airflow + Docker + MLOps deployment.",
     "github": "#", "live": "#"}
]

cols = st.columns(3)
for i, proj in enumerate(projects):
    with cols[i]:
        st.markdown(f"""
        <div class="card">
            <h4>{proj['title']}</h4>
            <p>{proj['desc']}</p>
            <a href="{proj['github']}">GitHub</a> | <a href="{proj['live']}">Live Demo</a>
        </div>
        """, unsafe_allow_html=True)

# ----- EXPERIENCE -----
st.markdown("## 💼 Experience")
st.timeline = [
    {"time": "2023 - Present", "role": "Data Scientist @ TCS"},
    {"time": "2021 - 2023", "role": "ML Engineer @ StartupX"},
]
for exp in st.timeline:
    st.markdown(f"- **{exp['time']}** → {exp['role']}")

# ----- CONTACT -----
st.markdown("## 📬 Contact")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("✅ Message sent successfully!")

st.markdown("📌 [LinkedIn](#) | [GitHub](#) | [Kaggle](#)")
