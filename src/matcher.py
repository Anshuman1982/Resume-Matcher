from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import clean_text
import re

# Skill extraction function
def extract_skills(text):
    skills = [
        'python', 'pandas', 'numpy', 'machine learning', 'deep learning', 'data analysis',
        'data visualization', 'matplotlib', 'seaborn', 'scikit-learn', 'tensorflow',
        'keras', 'sql', 'nlp', 'excel', 'power bi', 'jupyter notebook',
        'communication', 'team collaboration', 'problem solving'
    ]
    text = text.lower()
    return list({skill for skill in skills if skill in text})


# Skill match % calculator
def get_skill_match(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    matched = list(set(resume_skills) & set(jd_skills))
    percent = (len(matched) / len(jd_skills)) * 100 if jd_skills else 0
    return matched, jd_skills, percent


#  Main function to match resume and JD
def match_resume_to_job_description(resume_text, jd_text):
    # Preprocess
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    # Vectorize
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, jd_clean])

    # Similarity Score
    similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0]

    # Skill Match
    matched_skills, jd_skills, skill_percent = get_skill_match(resume_text, jd_text)

    return similarity_score, matched_skills, jd_skills, skill_percent
