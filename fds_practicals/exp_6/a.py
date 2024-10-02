"""
Write a program to count the frequency of occurance of a word in a body of text is often
need during text processing
"""
import nltk
nltk.download("gutenberg")
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg
def word_frequency():
    sample = gutenberg.raw("blake-poems.txt")
    token = word_tokenize(sample)
    wlist = []
    for i in range(50):
        wlist.append(token[i])
    wordfreq = [wlist.count(w) for w in wlist]