from transformers import pipeline
classifier = pipeline("text-classification", model="bert-base-uncased")
result = classifier("I love using Hugging Face Transformers!")
print(result)
