
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
