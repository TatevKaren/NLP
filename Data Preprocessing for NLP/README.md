

## Step 1: Transforming to lowercase data
<img width="624" alt="Screenshot 2023-01-27 at 10 41 16 PM" src="https://user-images.githubusercontent.com/76843403/215251147-3bb8a91e-df7c-4637-86ad-dd2605833934.png">

## Step 2:  Removing space, digits, non-word, and single word characters
<img width="627" alt="Screenshot 2023-01-27 at 10 38 33 PM" src="https://user-images.githubusercontent.com/76843403/215250996-70342c90-6e6f-4a43-944b-09b941e2f2b0.png">

## Step 3: Tokenization
<img width="623" alt="Screenshot 2023-01-27 at 10 39 41 PM" src="https://user-images.githubusercontent.com/76843403/215251047-f17ddc2e-c327-4483-906c-ace96915d6a4.png">

## Step 4: Removing punctuation 
<img width="618" alt="Screenshot 2023-01-27 at 10 40 13 PM" src="https://user-images.githubusercontent.com/76843403/215251076-1c7958d1-9e65-4017-8364-21c79382ff02.png">


## Step 5: Stopword removal
<img width="615" alt="Screenshot 2023-01-27 at 10 40 34 PM" src="https://user-images.githubusercontent.com/76843403/215251090-b9829745-a0b7-4350-b1c5-835cc5472c15.png">






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
            
