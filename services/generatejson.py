import json
from Model import Model
from collections import Counter

# JsonUtil
class JSONUtil:
		
	# generateJson

	def generateJson(self,outputDictionary,analyzeData,key):
		inner_json_list = []
		questions = analyzeData[key]
		for question in questions:
			answers = outputDictionary[question]
			dict_of_answers =  dict(Counter(answers))
			DataModel = Model(key,question,dict_of_answers) 	
			DataModelJson = DataModel.toJson()
			inner_json_list.append(DataModelJson)
		inner_json = json.dumps({'data':inner_json_list})	
		return inner_json
