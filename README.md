# AI-Powered-Question-Generation-System

## Objective

To develop an intelligent system that automatically generates quizzes, assessments, and practice questions from educational content.

## Features

* Automatic Question Generation
* Answer Generation
* Explanation Generation
* Multiple Choice Question (MCQ) Generation
* Difficulty Level Classification
* Topic and Subject Categorization
* Question Validation
* JSON Output Generation
* FastAPI-based API Integration
* API Testing using Thunder Client

## Technologies Used

* Python
* FastAPI
* Transformers (FLAN-T5)
* PyTorch
* Uvicorn

## Project Structure

AI-Powered Question Generation System/

* api/
* services/
* main.py
* requirements.txt
* assessment_output.json
* README.md

## API Endpoint

### Generate Assessment

**POST** `/generate`

Sample Input:

```json
{
  "context": "Artificial Intelligence is a branch of computer science that enables machines to learn and make decisions."
}
```

Sample Output:

```json
{
  "question": "...",
  "answer": "...",
  "difficulty": "...",
  "mcq": {...}
}
```

## Performance Metrics

* Question Generation: Successful
* Answer Generation: Successful
* MCQ Generation: Successful
* Question Validation: Implemented
* API Testing: Passed
* Average Response Time: Approximately 1.2 seconds

## Expected Outcome

The system automatically generates high-quality assessments, reduces manual effort, and enhances the learning experience for students and educators.
