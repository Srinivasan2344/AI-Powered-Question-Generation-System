import random

def generate_mcq(question, answer):

    options = [
        answer,
        "Option B",
        "Option C",
        "Option D"
    ]

    random.shuffle(options)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer
    }