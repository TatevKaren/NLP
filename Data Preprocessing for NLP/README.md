

## Step 1: Transforming to lowercase data
<img width="623" alt="Screenshot 2023-01-27 at 10 37 52 PM" src="https://user-images.githubusercontent.com/76843403/215250957-71cd6c90-63ab-4e33-abbf-38f58b8e8853.png">

## Step 2:  Removing space, digits, non-word, and single word characters
<img width="627" alt="Screenshot 2023-01-27 at 10 38 33 PM" src="https://user-images.githubusercontent.com/76843403/215250996-70342c90-6e6f-4a43-944b-09b941e2f2b0.png">

## Step 3: Tokenization
![Uploading Screenshot 2023-01-27 at 10.39.04 PM.png…]()












## Text Cleaning in Python
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
            
