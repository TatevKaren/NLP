## Text Cleaning
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
            
