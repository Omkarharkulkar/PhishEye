import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load dataset
def load_dataset(urls_path, labels_path):
    urls_df = pd.read_csv(urls_path)
    labels_df = pd.read_csv(labels_path)
    return urls_df['url'], labels_df['label']

# Paths to your data (make sure these paths are correct)
urls_path = 'C:\\Users\\harku\\OneDrive\\Desktop\\PhishEye\\data\\urls.csv'
labels_path = 'C:\\Users\\harku\\OneDrive\\Desktop\\PhishEye\\data\\labels.csv'

# Load the dataset
urls, labels = load_dataset(urls_path, labels_path)

# Initialize the vectorizer and transform the dataset
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(urls)
y = labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Ensure the models directory exists
model_dir = 'backend/models'
os.makedirs(model_dir, exist_ok=True)

# Save the model using joblib
joblib.dump(model, os.path.join(model_dir, 'phishing_model.pkl'))
# Save the vectorizer
joblib.dump(vectorizer, os.path.join(model_dir, 'vectorizer.pkl'))

print("Model and vectorizer trained and saved successfully.")
