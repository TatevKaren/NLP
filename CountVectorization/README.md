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

