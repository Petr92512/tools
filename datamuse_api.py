import requests as rq
import json


class Synonyms():
	def __init__(self, word):
		self.word = word
	
	def rhyming_word(self):
		baseurl = "https://api.datamuse.com/words"
		params_dic = {}
		params_dic["rel_syn"] = self.word
		params_dic["max"] = "5"
		res = rq.get(baseurl , params = params_dic)
		#print(params_dic)
		words = [i for i in res.json()]
		return [word['word'] for word in words]

	def __repr__(self):
		return f"Object for {self.word}'s Synonyms"
    