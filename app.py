from flask import Flask, render_template, request
from resume_analyzer import analyze_resume
import os

app = Flask(__name__)
UPLOAD_FOLDER = "resumes/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return "No file uploaded!"
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file!"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Analyze resume
    result = analyze_resume(filepath)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
