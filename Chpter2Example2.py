3.	import nltk
4.	nltk.download('punkt_tab')
5.	from nltk.corpus import stopwords
6.	
7.	nltk.download('stopwords')
8.	
9.	text = "In the nineteenth century, the industrial revolution created profound social changes."
10.	tokens = nltk.word_tokenize(text.lower())  # تبدیل به حروف کوچک
11.	stop_words = set(stopwords.words('english'))
12.	filtered_tokens = [word for word in tokens if word not in stop_words and word.isalpha()]  # حذف کلمات توقف و علانم
13.	print(filtered_tokens)
