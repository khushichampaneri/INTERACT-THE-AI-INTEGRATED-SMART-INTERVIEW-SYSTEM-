answers = []


def save_answer(answer):
    answers.append(answer)


def get_answers():
    return answers


def clear_answers():
    answers.clear()


def evaluate_answer(question, answer):

    technical = 0

    grammar = 80

    communication = 80

    answer = answer.lower()

    keywords = question.lower().split()

    matched = 0

    for word in keywords:

        if word in answer:

            matched += 1

    technical = min(matched * 10, 100)

    if len(answer.split()) > 40:
        communication = 95
    elif len(answer.split()) > 25:
        communication = 85
    elif len(answer.split()) > 10:
        communication = 75
    else:
        communication = 60

    if "." in answer:
        grammar += 10

    overall = int(
        technical * 0.5 +
        grammar * 0.2 +
        communication * 0.3
    )

    if overall >= 80:
        level = "hard"

    elif overall >= 60:
        level = "medium"

    else:
        level = "easy"

    return {

        "technical": technical,

        "grammar": grammar,

        "communication": communication,

        "overall": overall,

        "level": level

    }

def generate_feedback(result):

    feedback = []

    if result["technical"] >= 80:
        feedback.append("✅ Excellent technical answer.")
    elif result["technical"] >= 60:
        feedback.append("👍 Good technical knowledge.")
    else:
        feedback.append("⚠ Improve your technical explanation.")

    if result["grammar"] >= 85:
        feedback.append("✅ Good grammar.")
    else:
        feedback.append("⚠ Improve sentence structure.")

    if result["communication"] >= 85:
        feedback.append("🎤 Excellent communication.")
    else:
        feedback.append("💬 Speak more clearly and confidently.")

    if result["overall"] >= 85:
        feedback.append("🏆 Outstanding answer!")
    elif result["overall"] >= 70:
        feedback.append("⭐ Good answer.")
    else:
        feedback.append("📚 More practice is recommended.")

    return feedback