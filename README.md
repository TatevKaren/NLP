# Natural Language Preprocessing (NLP)
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
            
## Counting Vetorization

        def count_vectorization(self):
           cv = CountVectorizer()
           cv_fit = cv.fit_transform(self.data['clean_text'])
           self.countMatrix = cv_fit.toarray()
           self.new_text_count = cv.transform(self.new_text).toarray()
           self.countMatrix_representation = pd.DataFrame(self.countMatrix_jobs,
                                                               columns = cv.get_feature_names(),
                                                               index = self.data['ID'])
           return(self.countMatrix, self.new_text_count)

## Obtain Cosine Similarities
     def getSimilarities(self):
         self.similarity = cosine_similarity(self.countMatrix, self.new_text_count)
         self.data["score"] = pd.Series(self.similarity.flatten())


## Get Top K, Most Similar Recommendation'
     def getTopKJobs(self):
         # sort the df based on score
         self.data = self.data.sort_values(by = 'score', ascending = False)
         self.TopK_results =  self.data[:self.K]
         print("Top {} Recommendations /n".format(self.K))
         print(self.TopK_jobs)







