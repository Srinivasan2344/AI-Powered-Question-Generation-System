from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load Model
model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# Generate Single Question
def generate_question(context):

    prompt = f"Generate a question from the following text: {context}"

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.8,
        top_k=50,
        top_p=0.95
    )

    question = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return question


# Generate Multiple Questions
def generate_multiple_questions(context, num_questions=3):

    questions = []

    attempts = 0

    while len(questions) < num_questions and attempts < 10:

        question = generate_question(context)

        if question and question not in questions:
            questions.append(question)

        attempts += 1

    return questions


# Test
if __name__ == "__main__":
    

    sample_context = """
    Artificial Intelligence is a branch of computer science
    that enables machines to learn, reason, and make decisions.
    """

    questions = generate_multiple_questions(sample_context)

    print("\nGenerated Questions:\n")

    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")