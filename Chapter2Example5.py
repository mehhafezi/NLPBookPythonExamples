6.	import nltk
7.	nltk.download('averaged_perceptron_tagger_eng')
8.	nltk.download('averaged_perceptron_tagger')
9.	nltk.download('punkt')
10.	
11.	text = "The cat is sleeping on the mat."
12.	tokens = nltk.word_tokenize(text)
13.	tagged = nltk.pos_tag(tokens)
14.	print(tagged)
