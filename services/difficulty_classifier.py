def classify_difficulty(question):


    words = len(question.split())

    if words < 8:
        return "Easy"
    elif words < 15:
        return "Medium"
    else:
        return "Hard"