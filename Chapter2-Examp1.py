import nltk # دانلود مدل (اگر قبلاً نکرده‌اید)
nltk.download('punkt')
text = "In the nineteenth century, the industrial revolution created profound social changes."
tokens = nltk.word_tokenize(text)
print(tokens)

