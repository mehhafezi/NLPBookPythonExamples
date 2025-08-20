5.	import spacy
6.	nlp = spacy.load("en_core_web_sm")
7.	doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")
8.	for ent in doc.ents:
9.	    print(f"{ent.text}: {ent.label_}")
