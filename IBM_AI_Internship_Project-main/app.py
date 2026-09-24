import streamlit as st
import pandas as pd

from utils.parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.role_recommender import recommend_roles
from utils.ats_matcher import calculate_ats_score
from utils.ai_suggestions import generate_ai_suggestions
from utils.ai_interview_generator import generate_ai_interview_questions
from utils.ai_career_roadmap import generate_ai_career_roadmap
from utils.market_analyzer import (
    load_market_data,
    get_top_market_skills,
    get_role_distribution,
    get_role_required_skills,
    get_relevant_jobs_count,
    generate_fact_insight_action,
)

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="Smart Career Assistant - Arjit Aggarwal",
    page_icon="🎯",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .author-badge {
        background-color: #EFF6FF;
        border-left: 4px solid #2563EB;
        padding: 8px 14px;
        border-radius: 4px;
        margin-bottom: 15px;
        font-size: 0.95rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
    .fact-box {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .insight-box {
        background-color: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .action-box {
        background-color: #ECFDF5;
        border-left: 4px solid #10B981;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .skill-tag {
        display: inline-block;
        background-color: #E2E8F0;
        color: #1E293B;
        padding: 4px 10px;
        border-radius: 12px;
        font-weight: 500;
        font-size: 0.85rem;
        margin: 2px 4px 4px 0px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load Naukri Market Dataset
market_df = load_market_data()

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/briefcase.png", width=64)
    st.title("Smart Career Assistant")
    st.markdown("**Author**: Arjit Aggarwal")
    st.markdown("**Project**: IBM AI Internship Project")
    st.markdown("---")

    st.subheader("📌 Project Overview")
    st.caption(
        "An AI-powered Smart Career Assistant aligning resumes with real-world "
        "Naukri Indian job market data (12,000+ listings), skill gap analysis, "
        "and Google Gemini AI guidance."
    )

    st.subheader("📊 Dataset Statistics")
    if not market_df.empty:
        st.metric("Total Jobs Indexed", f"{len(market_df):,}")
        st.metric("Top Role", "Data Scientist / Engineer")
    else:
        st.info("Dataset loading...")

    st.markdown("---")
    st.caption("Developed by Arjit Aggarwal | IBM AI Internship Masterclass")

# ---------------------------------------------------------
# Main Page Header
# ---------------------------------------------------------
st.markdown('<div class="main-title">🎯 Smart Career Assistant using AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Align your resume with 12,000+ Naukri Indian Job Market Listings & Gemini AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="author-badge">
        👨‍💻 <b>Developed By</b>: <b>Arjit Aggarwal</b> &nbsp;|&nbsp; 
        🎓 <b>IBM AI Internship Project</b> &nbsp;|&nbsp; 
        📈 <b>Powered by Naukri Market Dataset & Gemini AI</b>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Step 1: Resume Upload & Parsing
# ---------------------------------------------------------
st.header("📄 Step 1: Resume Upload & Parsing")

col_upload, col_sample = st.columns([3, 1])

with col_upload:
    uploaded_file = st.file_uploader("Upload your Resume (PDF format)", type=["pdf"])

with col_sample:
    st.write("&nbsp;")
    use_sample = st.button("📄 Use Sample Resume", help="Click to test instantly with a sample data science resume")

sample_resume_text = """
Arjit Aggarwal
Email: arjit@example.com | Mobile: +91-9876543210
Education: B.Tech in Computer Science & Engineering

Skills:
- Programming: Python, SQL, C++, HTML, CSS, JavaScript
- Data Science & ML: Machine Learning, Data Analysis, Pandas, NumPy, Scikit-Learn, Statistics
- Visualization & Tools: Tableau, Power BI, Git, Excel

Projects:
- Smart Career Assistant using AI: Built a Streamlit web app integrating spaCy skill extraction and job market data.
- Predictive Analytics Pipeline: Developed ML model in Python for customer churn prediction.
"""

resume_text = ""

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ Resume uploaded and parsed successfully!")
elif use_sample:
    resume_text = sample_resume_text
    st.info("💡 Using sample data science resume for analysis.")

if resume_text:
    # ---------------------------------------------------------
    # Skill Extraction
    # ---------------------------------------------------------
    skills = extract_skills(resume_text)

    # Calculate initial recommendations & target role
    recommendations = recommend_roles(skills, market_df)
    top_role = recommendations[0][0] if recommendations else "Data Scientist"
    top_score = recommendations[0][1] if recommendations else 0.0

    # Derive dynamic ATS skills from dataset for top role
    role_required_skills = get_role_required_skills(market_df, top_role, top_n=6)
    ats_result = calculate_ats_score(skills, role_required_skills)
    relevant_jobs = get_relevant_jobs_count(market_df, skills, top_role)

    # ---------------------------------------------------------
    # Step 2: Executive Dashboard KPIs
    # ---------------------------------------------------------
    st.markdown("---")
    st.header("📊 Step 2: Career Analysis Dashboard")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            label="🛠 Resume Skills Detected",
            value=f"{len(skills)} Skills",
            delta="Extracted via spaCy",
        )

    with kpi2:
        st.metric(
            label="🎯 Top Role Match",
            value=f"{top_score:.0f}%",
            delta=top_role,
        )

    with kpi3:
        st.metric(
            label="💼 Relevant Market Jobs",
            value=f"{relevant_jobs:,}",
            delta="Naukri Dataset",
        )

    with kpi4:
        st.metric(
            label="❌ Skill Gaps Identified",
            value=f"{len(ats_result['missing_skills'])} Skills",
            delta="For " + top_role,
            delta_color="inverse",
        )

    # Extracted Skills Display
    st.subheader("🛠 Extracted Skills from Resume")
    if skills:
        skill_html = "".join([f'<span class="skill-tag">✓ {s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
    else:
        st.warning("No skills detected in resume.")

    # ---------------------------------------------------------
    # Step 3: Job Market Insights
    # ---------------------------------------------------------
    st.markdown("---")
    st.header("📈 Step 3: Job Market Insights (Naukri Dataset)")

    m_col1, m_col2 = st.columns(2)

    with m_col1:
        st.subheader("🔥 Top In-Demand Market Skills")
        top_skills_data = get_top_market_skills(market_df, top_n=8)
        if top_skills_data:
            skill_chart_df = pd.DataFrame(top_skills_data).set_index("skill")
            st.bar_chart(skill_chart_df["percentage"], color="#2563EB")
            st.caption("Percentage of Naukri job listings requiring each skill.")

    with m_col2:
        st.subheader("💼 Relevant Job Role Distribution")
        role_dist_df = get_role_distribution(market_df, top_n=8)
        if not role_dist_df.empty:
            st.bar_chart(role_dist_df.set_index("Role")["Listings"], color="#10B981")
            st.caption("Distribution of job vacancies across top roles in India.")

    # ---------------------------------------------------------
    # Step 4: Role Matching & Dataset ATS Alignment
    # ---------------------------------------------------------
    st.markdown("---")
    st.header("🎯 Step 4: Role Recommendation & Dataset ATS Match")

    r_col1, r_col2 = st.columns(2)

    with r_col1:
        st.subheader("🏆 Recommended Job Roles")
        if recommendations:
            for role, score, job_cnt in recommendations:
                st.markdown(
                    f"• **{role}** → **{score:.0f}% Match** `({job_cnt:,} dataset jobs)`"
                )
        else:
            st.warning("No matching roles found.")

    with r_col2:
        st.subheader("📊 Dataset-Derived ATS Match Analysis")
        selected_role = st.selectbox(
            "Select Target Role for ATS Match:",
            options=[r[0] for r in recommendations] if recommendations else [top_role],
        )

        # Recalculate for selected role
        selected_req_skills = get_role_required_skills(market_df, selected_role, top_n=6)
        ats_result = calculate_ats_score(skills, selected_req_skills)

        st.metric(
            label=f"ATS Score for {selected_role}",
            value=f"{ats_result['score']}%",
        )

        st.write("✅ **Matched Skills:**", ", ".join(ats_result["matched_skills"]) if ats_result["matched_skills"] else "None")
        st.write("❌ **Missing Skills (Skill Gap):**", ", ".join(ats_result["missing_skills"]) if ats_result["missing_skills"] else "None")

    # ---------------------------------------------------------
    # Step 5: Insights & Recommendations (Fact -> Insight -> Action)
    # ---------------------------------------------------------
    st.markdown("---")
    st.header("🧠 Step 5: Insights & Recommendations")

    fia_data = generate_fact_insight_action(skills, selected_role, ats_result, market_df)

    st.markdown(f'<div class="fact-box">📌 {fia_data["fact"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="insight-box">💡 {fia_data["insight"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="action-box">🎯 {fia_data["action"]}</div>', unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Step 6: AI-Powered Career Guidance (Gemini AI)
    # ---------------------------------------------------------
    st.markdown("---")
    st.header("🤖 Step 6: AI Career Assistant (Google Gemini)")

    tab_sug, tab_int, tab_road = st.tabs([
        "💡 AI Career Suggestions",
        "🎤 AI Interview Questions",
        "🛣 AI 6-Month Roadmap",
    ])

    with tab_sug:
        st.subheader("💡 Tailored Career Suggestions")
        if st.button("Generate AI Suggestions", key="btn_sug"):
            with st.spinner("Generating AI suggestions using Gemini..."):
                suggestions = generate_ai_suggestions(skills, selected_role, ats_result["missing_skills"])
                st.markdown(suggestions)

    with tab_int:
        st.subheader("🎤 Role-Specific Interview Questions")
        if st.button("Generate Interview Questions", key="btn_int"):
            with st.spinner("Generating interview prep questions..."):
                questions = generate_ai_interview_questions(skills, selected_role)
                st.markdown(questions)

    with tab_road:
        st.subheader("🛣 Personalized 6-Month Career Roadmap")
        if st.button("Generate Career Roadmap", key="btn_road"):
            with st.spinner("Creating 6-month career roadmap..."):
                roadmap = generate_ai_career_roadmap(skills, selected_role, ats_result["missing_skills"])
                st.markdown(roadmap)

else:
    st.info("👆 Please upload a PDF resume or click 'Use Sample Resume' to unlock full analysis.")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.markdown(
    "<center><small>Developed by <b>Arjit Aggarwal</b> | IBM AI Internship Masterclass | "
    "Smart Career Assistant Project</small></center>",
    unsafe_allow_html=True,
)