import PyPDF2

skills_list = [

    # Programming
    "python","java","c","c++","c#","php","javascript","typescript",

    # Web
    "html","css","bootstrap","react","angular","vue","nodejs","express",

    # Database
    "sql","mysql","mongodb","postgresql","sqlite","oracle",

    # AI / ML
    "machine learning","deep learning","artificial intelligence",
    "tensorflow","keras","pytorch","opencv","scikit-learn",
    "pandas","numpy","matplotlib","seaborn","nlp","transformer",
    "cnn","rnn","lstm","yolo","deep sort",

    # Cloud
    "aws","azure","gcp","docker","kubernetes",

    # DevOps
    "git","github","linux","jenkins",

    # Data Science
    "power bi","tableau","excel",

    # Others
    "flask","django","fastapi","streamlit"

]


def parse_resume(filepath):

    text = ""

    with open(filepath, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return {

        "text": text,

        "skills": found_skills

    }