
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("C:/Users/LENOVO/Desktop/Placement_project/AI reccomendation project/data/internship_data.csv")

df = df.drop(['id','eligibility','source'], axis=1, errors="ignore")

#to run the project use this command :- uvicorn main:app --reload 

# Create combined text column
df["profile_text"] = (
    df["title"] + " " +
    df["domain"] + " " +
    df["skills"].str.replace(";", " ") + " " +
    df["description"]
)

# Initialize vectorizer
vectorizer = TfidfVectorizer(stop_words="english")

# Convert text to vectors
tfidf_matrix = vectorizer.fit_transform(df["profile_text"])


def recommend_by_text(user_query, top_n=6):

    query_vector = vectorizer.transform([user_query])

    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

    top_indices = similarity_scores.argsort()[::-1][:top_n]

    # IMPORTANT: create copy
    results = df.iloc[top_indices].copy()

    # ADD match_score column
    results["match_score"] = similarity_scores[top_indices]

    return results

