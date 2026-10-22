job_roles = {

    "AI/ML Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "opencv",
        "git",
        "docker"
    ],

    "Python Developer": [
        "python",
        "flask",
        "sql",
        "git"
    ],

    "Cloud Engineer": [
        "aws",
        "docker",
        "linux",
        "git"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "machine learning"
    ]

}


def skill_gap(user_skills, role):

    required = job_roles.get(role, [])

    have = []
    missing = []

    for skill in required:

        if skill in user_skills:
            have.append(skill)
        else:
            missing.append(skill)

    score = int(len(have) / len(required) * 100) if required else 0

    return {

        "have": have,
        "missing": missing,
        "score": score

    }