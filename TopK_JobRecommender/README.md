## Get Top K, Most Similar Recommendation'
     def getTopKJobs(self):
         # sort the df based on score
         self.data = self.data.sort_values(by = 'score', ascending = False)
         self.TopK_results =  self.data[:self.K]
         print("Top {} Recommendations /n".format(self.K))
         print(self.TopK_jobs)
