import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from src.skill_gap import find_skill_gap
from src.recommender import recommend_skills
from src.roadmap_generator import generate_roadmap


# PAGE CONFIG
st.set_page_config(
    page_title="Universal Skill Gap Analyzer",
    page_icon="🎓",
    layout="wide"
)

# LOAD DATA
data = pd.read_csv("data/job_dataset.csv")


# HEADER
st.title("🎓 Universal AI Career Mentor")
st.write("Analyze your skills and compare them with real industry requirements across multiple departments.")

st.divider()

# DEPARTMENT SELECTION
department = st.selectbox(
    "Select Your Department",
    data["department"].unique()
)

# FILTER JOBS BASED ON DEPARTMENT
dept_jobs = data[data["department"] == department]

col1, col2 = st.columns(2)

with col1:
    skills_input = st.text_input(
        "Enter your skills (comma separated)",
        placeholder="Example: Python, CAD, AutoCAD"
    )

with col2:
    job = st.selectbox(
        "Select Target Job Role",
        dept_jobs["job_title"]
    )

st.divider()


# ANALYZE BUTTON
if st.button("🚀 Analyze Skill Gap", use_container_width=True):

    if skills_input == "":
        st.warning("Please enter your skills.")
        st.stop()

    user_skills = skills_input.split(",")

    job_skills = dept_jobs[dept_jobs["job_title"] == job]["skills"].values[0].split(",")

    missing_skills, match = find_skill_gap(user_skills, job_skills)

    st.subheader("📊 Skill Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Skill Match", f"{match}%")

    with col2:
        st.metric("Your Skills", len(user_skills))

    with col3:
        st.metric("Missing Skills", len(missing_skills))

    st.divider()

    # PIE CHART
    chart = pd.DataFrame({
        "Category": ["Matched", "Missing"],
        "Value": [match, 100-match]
    })

    fig = px.pie(
        chart,
        values="Value",
        names="Category",
        title="Skill Match Distribution",
        hole=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # SKILL COMPARISON TABLE
    st.subheader("📋 Skill Comparison")

    comparison = []

    for skill in job_skills:

        skill = skill.strip()

        if skill.lower() in [s.strip().lower() for s in user_skills]:
            status = "✅ Have"
        else:
            status = "❌ Missing"

        comparison.append({
            "Skill": skill,
            "Status": status
        })

    df = pd.DataFrame(comparison)

    st.dataframe(df, use_container_width=True)

    st.divider()

    # RECOMMENDATIONS
    st.subheader("📚 Learning Recommendations")

    rec = recommend_skills(missing_skills)

    for r in rec:
        st.write("•", r)

    st.divider()

    # ROADMAP
    st.subheader("🗺 Career Roadmap")

    roadmap = generate_roadmap(missing_skills)

    for step in roadmap:
        st.write("•", step)

    st.success(f"🎯 Follow this roadmap to become a successful {job}!")