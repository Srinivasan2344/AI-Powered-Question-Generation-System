from datasets import load_dataset

dataset = load_dataset("squad")

print(dataset)
print(dataset["train"][0])