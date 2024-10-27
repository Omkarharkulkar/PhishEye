# PhishEye: Real-Time Phishing Detection Browser Extension

**PhishEye** is a real-time phishing detection browser extension designed to safeguard users from phishing attempts while they browse email links online. Leveraging machine learning and Natural Language Processing (NLP), PhishEye actively scans URLs in emails, analyzing patterns to detect phishing threats instantly. It provides real-time alerts, helping users identify and avoid phishing attacks effectively.

## 📌 Project Uniqueness and Newness

PhishEye is unique in its ability to combine NLP and machine learning for phishing detection, specifically targeting email links. Unlike traditional methods that rely heavily on blacklists or purely signature-based detection, PhishEye uses real-time data processing and URL pattern recognition to detect emerging phishing techniques. This approach allows it to detect "zero-day" phishing attempts, setting it apart from other browser extensions or detection systems.

## 🌟 Key Features

- **Real-Time Detection**: Identifies phishing threats instantly while browsing email links.
- **Machine Learning**: Uses Logistic Regression for accurate phishing detection.
- **NLP-Powered Analysis**: Extracts features from email content and URLs for analysis.
- **User-Friendly Interface**: Designed as a browser extension for easy accessibility.
- **Cross-Browser Compatibility**: Can be adapted for multiple browsers, adding versatility.

## ✅ Pros

- **High Detection Accuracy**: Thanks to its machine learning foundation, it detects phishing threats with high accuracy.
- **Real-Time Alerts**: Users receive immediate alerts when suspicious links are identified.
- **Adaptable to New Phishing Tactics**: Using NLP and pattern recognition, it adapts better to evolving phishing methods.

## ❌ Cons

- **Data Dependency**: The effectiveness depends on the quality and variety of training data.
- **Browser-Specific Implementation**: Requires adaptation for each browser environment.
- **Limited to Email Links**: Currently focuses on email links, so phishing attempts outside this scope may not be detected.

## 📂 Project Structure


## ⚙️ Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/PhishEye.git
    cd PhishEye
    ```

2. **Install Dependencies**:
   - Ensure you have Python 3.x installed.
   - Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Configuration**:
   - Edit `config.json` to specify the paths for `phishing_model.pkl`, `vectorizer.pkl`, and data files.

4. **Train the Model (Optional)**:
   - If you want to retrain the model, ensure `urls.csv` and `labels.csv` are in the `data/` directory and run:
     ```bash
     python backend/train_model.py
     ```

5. **Run the Application**:
   - To start the phishing detection service:
     ```bash
     python main.py
     ```
   - Load the extension:
     - Open your browser’s extension settings.
     - Enable Developer Mode and load `browser_extension/` as an unpacked extension.

## 🚀 Usage

Once the extension is loaded, PhishEye will begin monitoring URLs in emails. Upon detecting a phishing attempt, a real-time alert will be triggered to warn the user.

## 🛠 Technologies Used

- **Programming Language**: Python, JavaScript
- **Libraries**: Scikit-Learn, TfidfVectorizer, Flask
- **Machine Learning Model**: Logistic Regression

## 📈 Future Improvements

- Implement support for additional types of phishing attempts beyond email.
- Enhance the model by integrating a deep learning approach for increased accuracy.
- Improve cross-browser compatibility for broader user accessibility.

## 🤝 Contributing

Contributions are welcome! For significant changes, please open an issue first to discuss your idea.
