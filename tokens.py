import nltk
nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
sentence = "Hello there! How are you doing today?"
tokens = word_tokenize(sentence)
print(tokens)

bigrams = list(ngrams(tokens, 3))
print(bigrams)