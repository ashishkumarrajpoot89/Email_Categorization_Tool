# 📧 Email Categorization Tool

The **Email Categorization Tool** is a machine learning-powered application that classifies emails into predefined categories (e.g., Work, Personal, Promotions) using **Natural Language Processing (NLP)** techniques.  
It helps users organize their inbox automatically, collect feedback on categorization accuracy, and visualize performance metrics.  

🚀 **Live App:** [Click here to use the tool](https://emailcategorizationtool-ssffgyajzmcuqljuyoxn7a.streamlit.app/)  

---

## 📌 Features

- **NLP-based Classification** – Uses text preprocessing, TF-IDF vectorization, and ML models to classify emails.  
- **Interactive Streamlit UI** – User-friendly interface for entering email text and viewing predictions.  
- **SQL Feedback Storage** – Stores user feedback on classification results for continuous model improvement.  
- **Performance Visualization (Tableau)** – Displays metrics such as accuracy, precision, recall, and confusion matrix via Tableau dashboards.  

---

## 🛠️ Tech Stack

**Languages & Libraries**  
- Python (NLTK, Scikit-learn, Pandas, NumPy)  
- Streamlit (for deployment)  
- SQL (MySQL/PostgreSQL for storing feedback)  

**Visualization**  
- Tableau (for performance analytics)  

---

## 📂 Project Structure

```
Email Categorization Tool/
│
├── app.py                # Streamlit app code
├── model.pkl             # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
├── db_connection.py      # SQL connection & feedback storage
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── data/                 # Dataset & preprocessing files
```

---

## ⚙️ How It Works

1. **User Input** – Enter the email text in the Streamlit interface.  
2. **Preprocessing** – Remove stopwords, punctuation, and apply TF-IDF vectorization.  
3. **Prediction** – ML model predicts the category.  
4. **Feedback Collection** – User confirms if classification is correct, which is stored in the SQL database.  
5. **Performance Tracking** – Tableau dashboard visualizes model performance over time.  

---

## 📊 Tableau Dashboard

🔗 *Add Tableau dashboard link here once published*  

---

## ▶️ Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/email-categorization-tool.git
cd email-categorization-tool

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 📌 Future Improvements

- Add more email categories.  
- Implement deep learning models (BERT, RoBERTa).  
- Support multiple languages.  
- Auto-refresh Tableau dashboard with latest feedback data.  

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
