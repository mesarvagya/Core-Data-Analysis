__author__ = "Sarvagya Pant"
import numpy as np
class BagOfWordClassifier:
	'''
	The code is based on Core Concept in Data Analysis on Coursera.
	The code tries to find the appropriate cluster based upon the data earlier
	and given querylist.
	Usage
	>>>b = BagOfWordClassifier("datas.txt"," ")
	>>>print b.bayes_classifier(3,[4,8,12],[1,1,2,1,1,0,0,1,0,0])
	..... I think the query list belongs to #2 cluster and the matches are [17.633361687639272, 20.520137010619507, 17.105300933216817] 	
	'''
	def __init__(self, filename, delimiter):
		self.file = filename
		self.delimiter = delimiter

	def generate_table(self):
		'''
		Use for generating a table
		>>>generate_table("data.txt"," ")
		'''
		self.table = np.loadtxt(fname=self.file, delimiter=self.delimiter)
		return self.table

	def bag_of_words_classifier(self, num_clusters, indexes, query_list):
		"""
		Give numbers of clusters , indexes of data where clusters end
		and the query_list
		bayes_classifier
		>>>bayes_classifier(2,[1,6])
		"""
		row = []
		data = self.generate_table()
		bag_size = len(data[0])
		clusters = np.split(data, indexes)
		for i in range(len(clusters)-1):
			cluster_sum = np.sum(clusters[i]) + bag_size
			temp = []
			for j in range(bag_size):				
				sum_col =  np.sum(clusters[i][:,j]) + 1
				prob = sum_col / cluster_sum
				temp.append(prob)
			row.append(temp)
		row = np.array(row)
		row = np.log(row*100)
		c = np.log(100.0/num_clusters)
		query = np.array(query_list)
		res = map(lambda x: np.sum(x*query)+c, row)
		maximum_match = max(res)
		maximum_match_index = res.index(maximum_match) + 1
		msg = """I think the query list belongs to #%s cluster and the matches are %s \
		""" %(maximum_match_index,res)
		return msg

b = BagOfWordClassifier("datas.txt"," ")
print b.bag_of_words_classifier(3,[4,8,12],[1,1,2,1,1,0,0,1,0,0])