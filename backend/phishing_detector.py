# phishing_detector.py - Detects phishing based on extracted features
import joblib

class PhishingDetector:
    def __init__(self, model_path='models/phishing_model.pkl'):
        # Load the pre-trained model
        self.model = joblib.load(model_path)

    def predict(self, features):
        # Predict if the URL is phishing or not
        feature_vector = [features[key] for key in sorted(features.keys())]
        prediction = self.model.predict([feature_vector])[0]
        return 'phishing' if prediction == 1 else 'safe'
