import json

from services.explanation_generator import generate_explanation
from services.question_generator import generate_question, generate_multiple_questions
from services.answer_generator import generate_answer
from services.mcq_generator import generate_mcq
from services.difficulty_classifier import classify_difficulty
from services.dataset_loader import load_squad_sample
from services.question_validator import validate_question

def categorize_topic(text):

    text = text.lower()

    if "artificial intelligence" in text:
        return "Artificial Intelligence"
    elif "machine learning" in text:
        return "Machine Learning"
    elif "deep learning" in text:
        return "Deep Learning"
    else:
        return "General"


def categorize_subject(text):

    text = text.lower()

    if any(word in text for word in ["computer", "artificial intelligence", "programming"]):
        return "Computer Science"
    elif any(word in text for word in ["plant", "photosynthesis", "biology"]):
        return "Biology"
    elif any(word in text for word in ["atom", "chemical", "chemistry"]):
        return "Chemistry"
    elif any(word in text for word in ["force", "energy", "physics"]):
        return "Physics"
    else:
        return "General"


def main():

    context = """
    Artificial Intelligence is a branch of computer science that enables machines
    to learn, reason, and make decisions.
    """

    question = generate_question(context)

    is_valid = validate_question(question)

    answer = generate_answer(context, question)

    mcq = generate_mcq(question, answer)

    difficulty = classify_difficulty(question)

    questions = generate_multiple_questions(context)

    # Temporary Explanation
    explanation = generate_explanation(answer)

    topic = categorize_topic(context)

    subject = categorize_subject(context)

    result = {
    "context": context.strip(),
    "question": question,
    "question_valid": is_valid,
    "answer": answer,
    "explanation": explanation,
    "difficulty": difficulty,
    "topic": topic,
    "subject": subject,
    "question_type": "MCQ",
    "mcq": mcq
}

    with open("assessment_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(json.dumps(result, indent=4, ensure_ascii=False))

    print("\nGenerated Questions:")

    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")


if __name__ == "__main__":
    main()