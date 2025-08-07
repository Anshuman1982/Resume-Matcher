import streamlit as st
import fitz  # PyMuPDF
from matcher import match_resume_to_job_description

# App Title
st.set_page_config(page_title="Resume Matcher", layout="wide")
st.title(" Resume Matcher")
st.write("Upload a resume and a job description to see how well they match.")

# File Uploads
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"], key="resume")

with col2:
    job_description_file = st.file_uploader("Upload Job Description (PDF or TXT)", type=["pdf", "txt"], key="job")


def read_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text


def read_txt(file):
    return file.read().decode("utf-8")


if resume_file and job_description_file:
    with st.spinner("Extracting and analyzing..."):
        # Read Resume
        resume_text = (
            read_pdf(resume_file)
            if resume_file.type == "application/pdf"
            else read_txt(resume_file)
        )

        # Read Job Description
        job_description_text = (
            read_pdf(job_description_file)
            if job_description_file.type == "application/pdf"
            else read_txt(job_description_file)
        )

        # Match and display results
        similarity_score, matched_skills, jd_skills, skill_percent = match_resume_to_job_description(
            resume_text, job_description_text
        )

        st.subheader("🔗 Match Summary")
        st.markdown(f"**Similarity Score:** {similarity_score:.2f}")
        st.markdown(f"**Skill Match:** {len(matched_skills)} / {len(jd_skills)} ({skill_percent:.2f}%)")

        st.subheader("📌 Matched Skills")
        if matched_skills:
            st.write(", ".join(matched_skills))
        else:
            st.write("No matching skills found.")

        st.subheader("📄 Resume Preview")
        st.text_area("Resume Text", resume_text, height=200)

        st.subheader("📝 Job Description Preview")
        st.text_area("Job Description Text", job_description_text, height=200)

else:
    st.info("Please upload both a resume and a job description to proceed.")
