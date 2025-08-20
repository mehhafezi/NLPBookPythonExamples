3.	import stanza
4.	stanza.download('fa')
5.	nlp = stanza.Pipeline('fa')
6.	doc = nlp("باراک اوباما در هاوایی متولد شد.")
7.	for sentence in doc.sentences:
8.	    for word in sentence.words:
9.	        print(f"Word: {word.text}, POS: {word.upos}")
