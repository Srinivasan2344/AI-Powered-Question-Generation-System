from datasets import load_dataset

dataset = load_dataset("allenai/sciq")

print(dataset)

from datasets import load_dataset

dataset = load_dataset("allenai/sciq")

print(dataset["train"][0])
print("Train Size:", len(dataset["train"]))
print("Validation Size:", len(dataset["validation"]))
print("Test Size:", len(dataset["test"]))

#dataset to mcq format
sample = dataset["train"][0]

mcq = {
    "question": sample["question"],
    "options": [
        sample["correct_answer"],
        sample["distractor1"],
        sample["distractor2"],
        sample["distractor3"]
    ],
    "correct_answer": sample["correct_answer"]
}

print(mcq)