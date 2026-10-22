import base64
import cv2
import numpy as np

from datetime import datetime
from reportlab.pdfgen import canvas
from flask import send_file
import os
from career_guidance import get_career_guidance
from skill_gap import skill_gap

from flask import jsonify
from emotion import detect_emotion
from eye_tracking import eye_contact
from voice_analysis import analyze_voice
from answer_analysis import evaluate_answer

from resume_score import calculate_resume_score

from answer_analysis import save_answer, get_answers, clear_answers
from answer_analysis import evaluate_answer, generate_feedback
from question_generator import generate_questions
from resume_parser import parse_resume
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from database import db, User, InterviewReport

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing = User.query.filter_by(email=email).first()

        if existing:
            flash("Email already exists!")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful!")
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session["user"] = user.name

            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password!")

    return render_template("login.html")


# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        user=session["user"]
    )


# ---------------- UPLOAD RESUME ---------------- #

# ---------------- UPLOAD RESUME ---------------- #

# ---------------- UPLOAD RESUME ---------------- #

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/upload_resume", methods=["GET", "POST"])
def upload_resume():

    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        file = request.files["resume"]

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        # Parse Resume
        result = parse_resume(filepath)
        session["skills"] = result["skills"]

        career_guidance = get_career_guidance(
        result["skills"]
)

        gap = skill_gap(
         result["skills"],
         "AI/ML Engineer"
)
        # Generate Interview Questions
        questions = generate_questions(result["skills"])

        # Calculate Resume Score
        resume_score = calculate_resume_score(
            result["skills"]
        )

        # Save data in session
        session["skills"] = result["skills"]
        session["resume_score"] = resume_score

        return render_template(
            "resume_result.html",
            skills=result["skills"],
            questions=questions,
            resume_score=resume_score,
            career_guidance=career_guidance,
            gap=gap
        )

    return render_template("upload_resume.html")

@app.route("/start_interview", methods=["POST"])
def start_interview():

    interview_type = request.form["type"]
    difficulty = request.form["difficulty"]

    session["interview_type"] = interview_type
    session["difficulty"] = difficulty

    # Temporary skills (later these will come from the uploaded resume)
    skills = ["python", "aws", "machine learning"]

    questions = generate_questions(skills)

    session["questions"] = questions
    session["question_index"] = 0

    question = questions[0]

    return render_template(
        "live_interview.html",
        interview_type=interview_type,
        difficulty=difficulty,
        question=question
    )

@app.route("/analyze_frame", methods=["POST"])
def analyze_frame():

    data = request.json["image"]

    image = data.split(",")[1]

    image = base64.b64decode(image)

    image = np.frombuffer(image, np.uint8)

    frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

    emotion = detect_emotion(frame)

    eye = eye_contact(frame)

    if emotion in ["happy", "neutral"]:
        confidence = 95
    elif emotion == "surprise":
        confidence = 85
    elif emotion == "fear":
        confidence = 65
    elif emotion == "sad":
        confidence = 60
    elif emotion == "angry":
        confidence = 55
    else:
        confidence = 75

    confidence = int((confidence + eye) / 2)

    # Save latest values in session
    session["emotion"] = emotion
    session["eye"] = eye
    session["confidence"] = confidence

    print("Emotion:", emotion)
    print("Eye:", eye)
    print("Confidence:", confidence)

    return jsonify({
        "emotion": emotion,
        "eye": eye,
        "confidence": confidence
    })

@app.route("/next_question", methods=["POST"])
def next_question():

    answer = request.form["answer"]

    save_answer(answer)

    questions = session["questions"]

    index = session["question_index"]

    current_question = questions[index]

    # AI Answer Evaluation
    result = evaluate_answer(current_question, answer)
    feedback = generate_feedback(result)
    print("AI Level :", result["level"])

    # Save all interview results
    if "results" not in session:
        session["results"] = []

    session["results"].append({

        "question": current_question,

        "answer": answer,

        "score": result

    })

    # Voice Analysis
    voice = analyze_voice(answer)

    # Live Analysis
    emotion = session.get("emotion", "Neutral")
    eye = session.get("eye", 0)
    confidence = session.get("confidence", 0)

    print(voice)
    print(confidence)

    # Next Question
    index += 1
    session["question_index"] = index

    if index >= len(questions):

        return redirect(url_for("final_report"))

    return render_template(
     "live_interview.html",
     interview_type=session["interview_type"],
     difficulty=session["difficulty"],
     question=questions[index],
     emotion=emotion,
     eye=eye,
     confidence=confidence,
     filler=voice["Filler Words"],
     speed=voice["Voice Speed"],
     feedback=feedback
)

    from datetime import datetime


@app.route("/final_report")
def final_report():

    results = session.get("results", [])

    emotion = session.get("emotion", "Neutral")
    eye = session.get("eye", 0)
    confidence = session.get("confidence", 0)

    total = 0

    for r in results:
        total += r["score"]["overall"]

    overall = int(total / len(results)) if results else 0

    # Calculate average scores
    technical = 0
    grammar = 0
    communication = 0

    if results:
        technical = int(sum(r["score"]["technical"] for r in results) / len(results))
        grammar = int(sum(r["score"]["grammar"] for r in results) / len(results))
        communication = int(sum(r["score"]["communication"] for r in results) / len(results))

    # Save report
    report = InterviewReport(
        user_name=session.get("user", "Guest"),
        overall=overall,
        emotion=emotion,
        eye=eye,
        confidence=confidence,
        date=datetime.now().strftime("%d-%m-%Y %H:%M")
    )

    db.session.add(report)
    db.session.commit()

    

    return render_template(
        "final_report.html",
        results=results,
        emotion=emotion,
        eye=eye,
        confidence=confidence,
        overall=overall,
        technical=technical,
        grammar=grammar,
        communication=communication
    )

# ---------------- INTERVIEW ---------------- #

@app.route("/interview")
def interview():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("interview.html")


# ---------------- REPORTS ---------------- #

@app.route("/reports")
def reports():

    reports = InterviewReport.query.order_by(
        InterviewReport.id.desc()
    ).all()

    return render_template(
        "reports.html",
        reports=reports
    )


# ---------------- PROFILE ---------------- #

@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("profile.html")


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

@app.route("/download_report")
def download_report():

    pdf_file = "Interview_Report.pdf"

    c = canvas.Canvas(pdf_file)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, 800, "AI Interview Report")

    c.setFont("Helvetica", 14)

    c.drawString(50, 760, f"Candidate : {session.get('user','User')}")
    c.drawString(50, 735, f"Overall Score : {session.get('overall',0)}%")
    c.drawString(50, 710, f"Emotion : {session.get('emotion','Neutral')}")
    c.drawString(50, 685, f"Eye Contact : {session.get('eye',0)}%")
    c.drawString(50, 660, f"Confidence : {session.get('confidence',0)}%")

    y = 620

    results = session.get("results", [])

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Interview Questions")

    y -= 30

    c.setFont("Helvetica", 12)

    for i, r in enumerate(results):

        c.drawString(50, y, f"Q{i+1}: {r['question']}")
        y -= 20

        c.drawString(70, y, f"Answer: {r['answer']}")
        y -= 20

        c.drawString(
            70,
            y,
            f"Score: {r['score']['overall']}%"
        )

        y -= 35

        if y < 80:
            c.showPage()
            y = 780

    c.save()

    return send_file(
        pdf_file,
        as_attachment=True
    )


# ---------------- MAIN ---------------- #

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=False)