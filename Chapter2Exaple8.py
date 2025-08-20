4.	import spacy
5.	nlp = spacy.load("en_core_web_sm")
6.	doc = nlp("Autonomous cars shift insurance liability toward manufacturers.")
7.	for token in doc:
8.	    print(f"{token.text}: dep={token.dep_}, head={token.head.text}")
