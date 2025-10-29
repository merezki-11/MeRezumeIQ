MeRezumeIQ

AI-Powered Resume Screening Tool

Overview

MeRezumeIQ is an AI-powered resume screening tool that leverages Natural Language Processing (NLP) and Machine Learning (ML) to analyze resumes and predict job-fit categories.

It helps automate the tedious process of manually reviewing resumes by understanding, categorizing, and ranking them, hence saving valuable time for HR teams, recruiters, and hiring managers.

Project Summary

This project trains a machine learning model on a dataset of resumes. The model learns to identify job categories based on the text content and can predict the most likely category for new, unseen resumes.

Project Structure

MeRezumeIQ.ipynb – Jupyter Notebook for model training and testing
app.py – Python script that loads the trained model and provides an interface for predictions
model.pkl, vectorizer.pkl – Serialized files containing the trained model and text vectorizer
UpdatedResumeDataSet.csv – Dataset used for training and testing the model.
How to Run Step 1: Clone the Repository git clone https://github.com/merezki-11/MeRezumeIQ.git cd MeRezumeIQ

Step 2: Install Dependencies Make sure you have Python 3.8+ installed, then run: pip install -r requirements.txt

Step 3: Run the App (Locally) Start the Streamlit or Flask app (depending on your version): streamlit run app.py Then open the displayed local URL (usually http://localhost:8501) to access the web interface.

Model Details

Text Preprocessing

Cleaned raw text using the re (Regular Expressions) library
Removed special characters, digits, and unnecessary whitespace
Converted text to lowercase for uniformity
Transformed text into numerical form using TF-IDF Vectorization
Model Training

Trained the model using LinearSVC from sklearn.svm
Split the dataset into training and testing sets
Evaluated performance using metrics like accuracy and F1-score
Saved the trained model as model.pkl and the vectorizer as vectorizer.pkl
Prediction

The model accepts raw resume text as input
Predicts the most suitable job category, such as:
Data Science
HR
Web Development
Software Engineering
Business Development
Example Output

Resume Text (Excerpt)	Predicted Category
"Developed predictive models using Python and Machine Learning"	Data Science
"Created responsive websites using HTML, CSS, and JavaScript"	Web Development
"Managed recruitment and employee relations"	HR
Future Improvements

Add a resume ranking system that compares resumes to specific job descriptions
Integrate real-time analytics for HR dashboards
Experiment with deep learning-based models (like BERT or RoBERTa) for improved accuracy
Include support for DOCX uploads alongside PDFs
Tech Stack

python
Pandas, NumPy – Data manipulation
Scikit-Learn – TF-IDF Vectorization, LinearSVC model
Streamlit – Web interface
pdfplumber – PDF text extraction
re (Regular Expressions) – Text cleaning and preprocessing
Author Macnelson Chibuike

macnelsonchibuike11@gmail.com

linkedin.com/in/macnelson-chibuike-b9126b292

github.com/merezki-11
