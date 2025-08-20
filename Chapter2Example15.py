!pip install nltk
 import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from textblob import TextBlob
blob = TextBlob("The book is great.")
print(blob.sentiment)
print(blob.tags)
