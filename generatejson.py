import json
import analyzeData
import textAnalytics
import getAnalyzedJson
from collections import Counter

# JsonUtil
class JSONUtil:
		
	# generateJson
	def generateJson(self,outputDictionary,analyzeData):
		inner_json_dict = []
		for key,value in analyzeData.iteritems():
			if key == 'opinion':
				for question in value:
					answers = outputDictionary[question]
					dict_of_answers =  dict(Counter(answers))
					analyzedJson = getAnalyzedJson.AnalyzedJson(key,question,dict_of_answers) 	
					analyzedJson = analyzedJson.toJson()
					inner_json_dict.append(analyzedJson)
					
			if key == 'scale':
				for question in value:
					answers = outputDictionary[question]
					dict_of_answers = dict(Counter(answers))
					analyzedJson = getAnalyzedJson.AnalyzedJson(key,question,dict_of_answers) 	
					analyzedJson = analyzedJson.toJson()
					#print analyzedJson
					inner_json_dict.append(analyzedJson)
			
			if key == 'analytics':
				for question in value:
					print question
					answers = outputDictionary[question]
					textAnalyticsObj = textAnalytics.TextAnalyzer()
					textAnalyticsObj.analyzeText(answers)

					


		inner_json = json.dumps({'data':inner_json_dict})	
