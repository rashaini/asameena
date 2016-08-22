from gensim import corpora
from nltk.corpus import stopwords

def index(filepath):
	stopwords = set(stopwords.words('english'))
	ps = PorterStemmer()

	# read formatted input
	documents = p.stem(word) for word in text.split()

	# convert documents into vectors