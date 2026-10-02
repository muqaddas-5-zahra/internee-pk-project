import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def extract_skills_and_experience(resume):
    doc = nlp(resume)

    skills_list = [
        "python", "java", "sql", "excel", "machine learning",
        "data science", "nlp", "tensorflow", "pandas",
        "numpy", "git", "github", "communication"
    ]

    text = resume.lower()

    skills = [skill for skill in skills_list if skill in text]

    experience = re.findall(
        r"\b\d+\+?\s*(?:years?|yrs?)\b",
        text
    )

    return skills, experience


def match_resume_to_job(resume, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")

    documents = [resume, job_description]
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return round(similarity * 100, 2)


# Example resume
resume = """
I am a data science intern with Python, SQL, Pandas,
Machine Learning and GitHub skills. I have 1 year of experience.
"""

# Example job description
job_description = """
We are looking for a Data Science Intern with Python,
SQL, Machine Learning and Pandas skills.
"""

skills, experience = extract_skills_and_experience(resume)
match_score = match_resume_to_job(resume, job_description)

print("Extracted Skills:", skills)
print("Experience:", experience)
print("Resume-Job Match Score:", match_score, "%")
