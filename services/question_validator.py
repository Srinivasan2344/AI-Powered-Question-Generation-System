def validate_question(question):

    if not question:
        return False

    if len(question.strip()) < 10:
        return False

    if not question.endswith("?"):
        return False

    return True