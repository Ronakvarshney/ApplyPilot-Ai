import os
import streamlit as st
from langgraph.types import Command

from resume_ingestion.ingestion import insert_resume
from app.graph.builder import chatbot, config


# ---------------------- Page Config ----------------------
st.set_page_config(
    page_title="ApplyPilot AI",
    page_icon="📧",
    layout="wide",
)

# ---------------------- Header ----------------------
st.title("🚀 ApplyPilot AI")
st.caption("Your AI-powered Job Application Copilot")

st.info(
"""
### Workflow

1. 📄 Upload Resume
2. 📋 Upload Job Description
3. 🧠 Resume Matching
4. 📊 Compatibility Analysis
5. ✉️ Generate Personalized Email
6. 📧 Send after Approval
"""
)

# ---------------------- Sidebar ----------------------
with st.sidebar:

    st.header("📂 Upload Files")

    resume_file = st.file_uploader(
        "Resume",
        type=["pdf", "docx"]
    )

    jd_file = st.file_uploader(
        "Job Description",
        type=["pdf", "docx"]
    )

    if resume_file:

        resume_path = os.path.join("uploads", resume_file.name)

        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())

        insert_resume(resume_file.name, resume_path)

        st.success("Resume uploaded.")

# ---------------------- JD Processing ----------------------
if jd_file:

    jd_path = os.path.join("uploads", jd_file.name)

    with open(jd_path, "wb") as f:
        f.write(jd_file.getbuffer())

    with st.spinner("Analyzing Resume..."):

        result = chatbot.invoke(
            {
                "source": jd_path
            },
            config=config
        )

    analysis = result["analysis"]

    st.success("Analysis Complete")

    # ---------------------- Metrics ----------------------

    c1, c2 = st.columns(2)

    with c1:
        st.metric("ATS Score", f"{analysis.ats_score}%")

    with c2:
        st.metric(
            "Selection Probability",
            f"{analysis.selection_probability}%"
        )

    st.divider()

    st.subheader("🎯 Recommendation")
    st.success(analysis.recommendation)

    st.subheader("📝 Overall Analysis")
    st.write(analysis.overall_analysis)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Strengths")

        if analysis.strengths:
            for s in analysis.strengths:
                st.markdown(f"- {s}")
        else:
            st.write("None")

    with col2:

        st.subheader("❌ Gaps")

        if analysis.gaps:
            for g in analysis.gaps:
                st.markdown(f"- {g}")
        else:
            st.write("None")

    st.subheader("💡 Suggested Improvements")

    if analysis.improvements:
        for i in analysis.improvements:
            st.markdown(f"- {i}")
    else:
        st.write("No suggestions.")

    st.divider()

    # ---------------------- Human Approval ----------------------

    snapshot = chatbot.get_state(config)

    if snapshot.interrupts:

        question = snapshot.interrupts[0].value["question"]

        st.subheader("🤖 Approval Required")

        st.info(question)

        decision = st.radio(
            "Your Decision",
            ["Yes", "No"],
            horizontal=True,
        )

        if st.button("Continue"):

            with st.spinner("Generating Email..."):

                result = chatbot.invoke(
                    Command(resume=decision.lower()),
                    config=config,
                )

            if "mail" in result:

                st.success("Email Generated")

                st.text_area(
                    "Generated Email",
                    result["mail"],
                    height=350,
                )

            else:

                st.warning("Email generation skipped.")
        
    
    