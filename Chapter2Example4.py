16.	import nltk
17.	from nltk.stem import WordNetLemmatizer
18.	
19.	nltk.download('wordnet')
20.	nltk.download('punkt')
21.	
22.	text = "better mice running"
23.	tokens = nltk.word_tokenize(text)
24.	lemmatizer = WordNetLemmatizer()
25.	lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
26.	print(lemmatized)
