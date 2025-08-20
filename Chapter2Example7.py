3.	import spacy
4.	nlp = spacy.load("en_core_web_sm")
5.	doc = nlp("Apple is looking at buying U.K. startup.")
6.	for token in doc:
7.	    print(f"{token.text}: {token.pos_}")
