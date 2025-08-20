import stanza
stanza.download('en')
nlp = stanza.Pipeline('en')
doc = nlp("Barack Obama was born in Hawaii.")
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"Word: {word.text}, POS: {word.upos}, Dep: {word.deprel}")