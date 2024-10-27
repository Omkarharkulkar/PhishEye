import os
import json
import logging
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Paths and settings from config.json
model_path = "C:\\Users\\harku\\OneDrive\\Desktop\\PhishEye\\backend\\backend\\models\\phishing_model.pkl"
vectorizer_path = "C:\\Users\\harku\\OneDrive\\Desktop\\PhishEye\\backend\\backend\\models\\vectorizer.pkl"
server_host = config['server']['host']
server_port = config['server']['port']
debug_mode = config['server']['debug_mode']

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the phishing detection model and vectorizer
def load_model():
    try:
        model = joblib.load(model_path)  # Load model using joblib
        vectorizer = joblib.load(vectorizer_path)  # Load vectorizer
        logging.info("Model and vectorizer loaded successfully.")
        return model, vectorizer
    except FileNotFoundError as e:
        logging.error(f"Error loading model/vectorizer: {e}")
        return None, None

model, vectorizer = load_model()

# Phishing detection route
@app.route('/detect', methods=['POST'])
def detect_phishing():
    if model is None or vectorizer is None:
        return jsonify({"error": "Model or vectorizer not initialized"}), 500

    data = request.get_json()
    if not data or 'urls' not in data:
        return jsonify({"error": "No URLs provided"}), 400

    urls = data['urls']
    if not isinstance(urls, list):
        return jsonify({"error": "URLs should be provided as a list"}), 400

    results = []
    for url in urls:
        url_features = vectorizer.transform([url])
        prediction = model.predict(url_features)
        result = "Phishing" if prediction[0] == 1 else "Legitimate"
        results.append({"url": url, "result": result})

    return jsonify(results)

# Run Flask server
if __name__ == '__main__':
    # Check if all necessary components are available
    if model is None or vectorizer is None:
        logging.error("Initialization failed due to missing components.")
    else:
        app.run(host=server_host, port=server_port, debug=debug_mode)
