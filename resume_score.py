def calculate_resume_score(skills):

    technical = min(len(skills) * 10, 100)

    ats = 70

    if len(skills) >= 8:
        ats += 20
    elif len(skills) >= 5:
        ats += 10

    project = 90 if len(skills) >= 6 else 75

    communication = 80

    overall = int(
        technical * 0.4 +
        ats * 0.3 +
        project * 0.2 +
        communication * 0.1
    )

    return {

        "technical": technical,

        "ats": ats,

        "projects": project,

        "communication": communication,

        "overall": overall

    }