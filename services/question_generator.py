from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_question(context):
    prompt = f"Generate a question from: {context}"

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def generate_multiple_questions(context, num_questions=3):
    """Generate multiple questions from a given context."""
    questions = []
    for i in range(num_questions):
        prompt = f"Generate a question from: {context}"
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=50)
        question = tokenizer.decode(outputs[0], skip_special_tokens=True)
        questions.append(question)
    return questions


contexts = [
    "Artificial Intelligence enables machines to learn and make decisions.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "Deep Learning uses neural networks to process data."
]

for text in contexts:
    print(generate_question(text))
question = generate_question(contexts[0])

print("Question:", question)
