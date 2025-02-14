# **📌 AI-Powered Resume Analyzer**  

## **🔍 Overview**  
The **AI-Powered Resume Analyzer** scans **PDF resumes**, extracts **skills, experience, and keywords**, and provides structured output. It uses **Natural Language Processing (NLP)** with **spaCy** and **regular expressions (Regex)** to extract relevant information.  

---

## **📜 Features**  
✅ **Extracts candidate name, email, phone, skills, and experience**  
✅ **Processes PDF resumes automatically**  
✅ **Uses NLP and regex for data extraction**  
✅ **Matches skills with job descriptions (future upgrade)**  
✅ **Flask web interface for uploading resumes**  

---

## **🚀 Installation**  

### **1️⃣ Install Dependencies**  
```sh
pip install spacy PyPDF2 flask
python -m spacy download en_core_web_sm
```

---

## **📂 File Structure**  
```
/AI_Resume_Analyzer
│── resume_analyzer.py     # Resume processing logic
│── app.py                 # Flask web app
│── templates
│   ├── index.html         # Web interface
│── resumes/               # Folder to store uploaded resumes
│── README.md              # Documentation
```


## **🔍 Running the Resume Analyzer**
### **1️⃣ Run the Flask Web App**
```sh
python app.py
```
### **2️⃣ Open in Browser**
Go to **http://127.0.0.1:5000/** to upload and analyze resumes.

---

## **📂 Example Resume Analysis Output**  

| **Field**   | **Extracted Data** |
|------------|------------------|
| **Email**  | `john.doe@gmail.com` |
| **Phone**  | `+91 9876543210` |
| **Skills** | `Python, SQL, Flask` |

---

## **⚠ Limitations & Ethics**  
⚠ The current skill extraction is based on predefined **keywords**.  
⚠ Regex-based **email/phone extraction** may miss some formats.  
⚠ AI models should be **trained on larger datasets** for better accuracy.  

---

## **🔧 Future Enhancements**  
✅ Use **Machine Learning (BERT)** for skill classification  
✅ Add **job matching AI** for resume ranking  
✅ Implement **cloud storage** for saving analyzed resumes  


