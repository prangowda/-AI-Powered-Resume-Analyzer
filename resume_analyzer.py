import spacy
import re
import PyPDF2

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to extract email, phone, and skills
def extract_details(text):
    details = {}

    # Extract email
    email_pattern = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+"
    details["email"] = re.findall(email_pattern, text)

    # Extract phone number
    phone_pattern = r"\b\d{10}\b|\+\d{1,2}\s?\d{10}"
    details["phone"] = re.findall(phone_pattern, text)

    # Extract skills from predefined list
    skill_keywords = ["Python", "Java", "C++", "Machine Learning", "Deep Learning", "SQL", "Flask", "Django"]
    doc = nlp(text)
    details["skills"] = [token.text for token in doc if token.text in skill_keywords]

    return details

# Main function to analyze resume
def analyze_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    details = extract_details(text)
    return details
