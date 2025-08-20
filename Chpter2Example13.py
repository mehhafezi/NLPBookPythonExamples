from gensim import corpora, models
documents = [["human", "interface", "computer"], ["survey", "user", "computer", "system", "response", "time"]]
dictionary = corpora.Dictionary(documents)
corpus = [dictionary.doc2bow(doc) for doc in documents]
lda = models.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)
print(lda.print_topics())
