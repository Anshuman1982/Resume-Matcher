import re
import os
import nltk
nltk.data.path.append("C:/Users/anshuman/AppData/Roaming/nltk_data")

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def clean_text(text):
    #convert to lowercase
    text = text.lower()

    #Remove non-alphabetic characters
    text = re.sub(r'[^a-z\s]','',text)
    
    #Tokenize
    tokens = word_tokenize(text)

    #Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered = [word for word in tokens if word not in stop_words]

    #Join back into a string
    return " ".join(filtered)

def read_file(relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # gets /src
    full_path = os.path.abspath(os.path.join(base_dir, "..", relative_path))
    print(f" Trying to open: {full_path}")
    with open(full_path, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == "__main__":
    sample = "This is just a simple test string, with punctuation!"
    cleaned = clean_text(sample)
    print("Cleaned output:", cleaned)

    # Actual resume + JD preprocessing
    resume_text = read_file("data/sample_resume/resume.txt")
    jd_text = read_file("data/sample_job_description/job_description.txt")

    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    print("\n Cleaned Resume Sample:\n", resume_clean[:500])
    print("\n Cleaned Job Description Sample:\n", jd_clean[:500])

