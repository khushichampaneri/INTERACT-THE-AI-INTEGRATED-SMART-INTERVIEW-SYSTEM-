def get_career_guidance(skills):

    guidance = []

    if "python" in skills:
        guidance.append({
            "career": "Python Developer",
            "salary": "₹4 - ₹12 LPA",
            "course": "Advanced Python & Flask",
            "companies": "TCS, Infosys, Cognizant"
        })

    if "machine learning" in skills:
        guidance.append({
            "career": "AI/ML Engineer",
            "salary": "₹8 - ₹20 LPA",
            "course": "Machine Learning Specialization",
            "companies": "Google, Microsoft, Amazon"
        })

    if "deep learning" in skills:
        guidance.append({
            "career": "Deep Learning Engineer",
            "salary": "₹10 - ₹25 LPA",
            "course": "Deep Learning with TensorFlow",
            "companies": "NVIDIA, OpenAI, Adobe"
        })

    if "aws" in skills:
        guidance.append({
            "career": "Cloud Engineer",
            "salary": "₹6 - ₹18 LPA",
            "course": "AWS Solutions Architect",
            "companies": "AWS, Accenture, IBM"
        })

    if "sql" in skills:
        guidance.append({
            "career": "Data Analyst",
            "salary": "₹5 - ₹12 LPA",
            "course": "SQL & Power BI",
            "companies": "Deloitte, EY, Capgemini"
        })

    if "opencv" in skills:
        guidance.append({
            "career": "Computer Vision Engineer",
            "salary": "₹8 - ₹22 LPA",
            "course": "Computer Vision with OpenCV",
            "companies": "Tesla, Bosch, Intel"
        })

    if len(guidance) == 0:
        guidance.append({
            "career": "Software Engineer",
            "salary": "₹4 - ₹10 LPA",
            "course": "DSA + Programming",
            "companies": "Infosys, Wipro, HCL"
        })

    return guidance