4.	import nltk
5.	nltk.download('punkt_tab')
6.	from nltk.stem import PorterStemmer
7.	
8.	nltk.download('punkt')
9.	
10.	text = "running runs ran runner"
11.	tokens = nltk.word_tokenize(text)
12.	stemmer = PorterStemmer()
13.	stemmed = [stemmer.stem(word) for word in tokens]
14.	print(stemmed)
