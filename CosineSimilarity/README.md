## Obtain Cosine Similarities
     def getSimilarities(self):
         self.similarity = cosine_similarity(self.countMatrix, self.new_text_count)
         self.data["score"] = pd.Series(self.similarity.flatten())

