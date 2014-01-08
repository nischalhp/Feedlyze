import readCsv
import analyzeData
import json
import getAnalyzedJson
import generatejson
from collections import Counter

readObj = readCsv.CSVReader('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
#now we a dictionary of questions and answers
data = readObj.getData()
analyzeObj = analyzeData.Analyzer(data)
analyzedData = analyzeObj.analyzeData()
#now we have analyzed data types , the questions and the answers to those question in data obj
#lets build a json of the type,question,answers
#so type is an array of questions, and questions has again an array of answers
generateJsonObj = generatejson.JSONUtil()		
#print analyzedData
jsonOp = generateJsonObj.generateJson(data,analyzedData)
	
#print json.dumps({'data':inner_json_dict})


		    
			




