# Importing necessary libraries
import pickle
import pdfplumber
import streamlit as st

#  PAGE CONFIGURATIONS

st.set_page_config(
    page_title="MerezumeIQ - An AI Resume Screening App",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Custom Page Style (Gradient Background + Modern UI) ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #87CEEB 30%, #E0F7FA 100%);
    color: #000000;
}

[data-testid="stHeader"] {
    background-color: rgba(255, 255, 255, 0.0);
}

[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #E0F7FA 30%, #FFFFFF 100%);
}

.main {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

h1, h2, h3 {
    color: #003366;
}

.stButton>button {
    background-color: #007ACC;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

.stTextArea textarea {
    background-color: #F9F9F9;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


# Main App Title
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("MerezumeIQ - An AI Resume Screening App")
st.write("Upload a PDF resume below, and watch the ResumeIQ classify it into the right category.")

# File uploader
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""

    if text.strip():
        st.subheader("Extracted Resume Text:")
        st.text_area("Preview", text[:1000], height=200)

        # Vectorize text and predict
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]
        st.success(f"✅ Predicted Category: {prediction}")

else:
    st.error("❌ Could not extract text. Try another Resume.")