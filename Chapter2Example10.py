import spacy
nlp = spacy.load("en_core_web_sm") # Changed model name to the one that was downloaded
doc = nlp("تهران پایتخت ایران است.")
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
