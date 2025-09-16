import streamlit as st
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention

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
        font-size: 1.3rem;
        color: #94a3b8;
        font-family: monospace;
    }
    .card {
        background: rgba(30, 41, 59, 0.7);
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 24px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ----- LOTTIE HELPER -----
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
data_lottie = load_lottie("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")  # data science animation

# ----- HERO -----
st.markdown("""
<div class="hero">
    <h1>Mohit Nayak</h1>
</div>
""", unsafe_allow_html=True)

# Typewriter effect
st.write("### _Turning Data into Decisions with AI & Machine Learning..._")

# Rain effect with emojis
rain(emoji="💡", font_size=24, falling_speed=5, animation_length="infinite")

# Hero animation
st_lottie(data_lottie, height=200, key="hero")

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.link_button("🚀 View My Work", "#projects")
with col2:
    st.link_button("📄 Download CV", "https://your-cv-link.com")

# ----- ABOUT -----
colored_header(label="👨‍💻 About Me", description=None, color_name="cyan-70")

col1, col2 = st.columns([1,2])
with col1:
    st.image("https://via.placeholder.com/200.png?text=Profile", width=200)
with col2:
    st.write("""
    Hi, I'm **Mohit Nayak**, a Data Scientist passionate about
    building end-to-end ML systems, creating interactive visualizations,
    and deploying models that solve real-world business problems.
    """)

# ----- SKILLS -----
colored_header(label="🛠 Skills", description=None, color_name="blue-70")

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
colored_header(label="🚀 Projects", description=None, color_name="green-70")

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
colored_header(label="💼 Experience", description=None, color_name="violet-70")
st.timeline = [
    {"time": "2023 - Present", "role": "Data Scientist @ TCS"},
    {"time": "2021 - 2023", "role": "ML Engineer @ StartupX"},
]
for exp in st.timeline:
    st.markdown(f"- **{exp['time']}** → {exp['role']}")

# ----- TESTIMONIALS -----
colored_header(label="💬 Testimonials", description=None, color_name="pink-70")
st.success("“Mohit is exceptional at simplifying complex data problems into actionable insights.” — Manager @ TCS")

# ----- CONTACT -----
colored_header(label="📬 Contact", description=None, color_name="gray-70")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("✅ Message sent successfully!")

# Social mentions
st.write("### 🌐 Connect with me:")
mention(label="LinkedIn", icon="linkedin", url="https://linkedin.com", write=False)
mention(label="GitHub", icon="github", url="https://github.com", write=False)
mention(label="Kaggle", icon="activity", url="https://kaggle.com", write=False)
