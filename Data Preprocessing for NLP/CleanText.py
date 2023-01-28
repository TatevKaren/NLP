'Cleaning the data'
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
import string
def clean_text(self, text):
    text = text.lower()
    text = re.sub("\d+", " ", text)
    text = re.sub("\W+", " ", text)
    text = word_tokenize(text)
    stopWords = stopwords.words("English")
    text = [word for word in text if word not in stopWords]
    text = [word for word in text if word not in string.punctuation]
    return ' '.join(text)

row_text = "Data science  % 67 8.. is related to Data Mining,     # @ Machine 5 Learning, Big Data, Computational Statistics and Analytics."
text = row_text.lower()
text = re.sub("\d+", " ", text)
text = re.sub("\W+", " ", text)
print(text)
from nltk import word_tokenize
text = word_tokenize(text)
print(text)


import string
text = ['&','data', 'science', 'is', 'related', 'to', 'data', 'mining', 'machine', 'learning', 'big', 'data', 'computational', 'statistics', 'and', 'analytics']
print(text)
text = [word for word in text if word not in string.punctuation]
print(text)

from nltk.corpus import stopwords
stopWords = stopwords.words("English")
text = [word for word in text if word not in stopWords]
print(text)
