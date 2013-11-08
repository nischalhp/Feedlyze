import readCsv
import analyzeData
import json
import getAnalyzedJson
readObj = readCsv.GetData('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
from collections import Counter
outputDictionary = readObj.getData()
analyzeObj = analyzeData.analyze(outputDictionary)
interpretation = analyzeObj.analyzeData()
output_json_list = []
inner_json_dict = []
for key,value in interpretation.iteritems():
	if key == 'opinion':
		for question in value:
			answers = outputDictionary[question]
			dict_of_answers =  dict(Counter(answers))
			# {"sty":"1", "op": }
			analyzedJson = getAnalyzedJson.AnalyzedJson(key,question,dict_of_answers) 	
			analyzedJson = analyzedJson.toJson()
			#print analyzedJson
			inner_json_dict.append(analyzedJson)
			
	if key == 'scale':
		for question in value:
			answers = outputDictionary[question]
			dict_of_answers = dict(Counter(answers))
			analyzedJson = getAnalyzedJson.AnalyzedJson(key,question,dict_of_answers) 	
			analyzedJson = analyzedJson.toJson()
			#print analyzedJson
			inner_json_dict.append(analyzedJson)
				
#print json.dumps({'data':inner_json_dict})


		    
			




