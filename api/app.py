from fastapi import FastAPI
from pydantic import BaseModel
import time

from services.question_generator import generate_question
from services.answer_generator import generate_answer
from services.mcq_generator import generate_mcq
from services.difficulty_classifier import classify_difficulty
from services.explanation_generator import generate_explanation

app = FastAPI()

class InputData(BaseModel):
    context: str

@app.post("/generate")
def generate_assessment(data: InputData):

    start = time.time()   # <-- Inga add pannu

    context = data.context

    question = generate_question(context)
    answer = generate_answer(context, question)
    mcq = generate_mcq(question, answer)
    difficulty = classify_difficulty(question)
    explanation = generate_explanation(answer)

    end = time.time()     # <-- Inga add pannu


    return {
        "context": context,
        "question": question,
        "answer": answer,
        "explanation": explanation,
        "difficulty": difficulty,
        "mcq": mcq,
        "response_time": f"{round(end - start, 2)} seconds"
    }