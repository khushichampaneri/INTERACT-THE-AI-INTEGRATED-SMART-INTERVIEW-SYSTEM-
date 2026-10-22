def analyze_voice(text):

    fillers = [

        "um",
        "uh",
        "like",
        "actually",
        "basically",
        "you know"

    ]

    total_words = len(text.split())

    filler_count = 0

    for word in fillers:

        filler_count += text.lower().count(word)

    if total_words < 30:

        speed = "Slow"

    elif total_words < 80:

        speed = "Normal"

    else:

        speed = "Fast"

    return {

        "Total Words": total_words,

        "Filler Words": filler_count,

        "Voice Speed": speed

    }