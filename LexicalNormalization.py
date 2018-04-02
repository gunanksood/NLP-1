from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()

word = raw_input("please enter a string ")

print lem.lemmatize(word, 'v')

print stem.stem(word)