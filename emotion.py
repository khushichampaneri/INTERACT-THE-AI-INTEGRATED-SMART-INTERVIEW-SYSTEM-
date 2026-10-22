from deepface import DeepFace

def detect_emotion(frame):

    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False,
            silent=True
        )

        return result[0]["dominant_emotion"]

    except Exception:
        return "neutral"