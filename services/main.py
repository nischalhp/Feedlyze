from flask import Flask
from flask import request
from flask import render_template
import readCsv
import analyzeData
import json

app = Flask(__name__)

@app.route('/')
def atHome():
	return render_template('index.html')

@app.route('/index.html')
def atBase():
	return render_template('index.html')

@app.route('/analyze/<path>')
def analyzeData(path):
	readCsvObj = readCsv.GetData(path)
	#now we a dictionary of questions and answers
	data = readCsvObj.getData()
	analyzeObj = analyzeData.analyze(data)
	analyzedData = analyzeObj.analyzeData()
	#now we have analyzed data types , the questions and the answers to those question in data obj
	#lets build a json of the type,question,answers
	#so type is an array of questions, and questions has again an array of answers
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
	inner_json = json.dumps({'data':inner_json_dict})			
			

if __name__=='__main__':
	app.run(debug=True)

