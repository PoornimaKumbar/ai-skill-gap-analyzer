import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load dataset
data = pd.read_csv("data/job_dataset.csv")

# Get skills column
skills = data["skills"]

# Convert text to vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(skills)

# Save model
joblib.dump(vectorizer, "models/skill_model.pkl")

print("Model trained and saved successfully")