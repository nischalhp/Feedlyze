from flask import Flask
from flask import request
from flask import render_template
import readCsv
import analyzeData
import json
import generatejson

app = Flask(__name__)

@app.route('/')
def atHome():
	return render_template('index.html')

@app.route('/index.html')
def atBase():
	return render_template('index.html')

@app.route('/analyze/<path>')
def analyzeData(path):
	readCsvObj = readCsv.CSVReader(path)
	#now we a dictionary of questions and answers
	data = readCsvObj.getData()
	analyzeObj = analyzeData.Analyzer(data)
	analyzedData = analyzeObj.analyzeData()
	#now we have analyzed data types , the questions and the answers to those question in data obj
	#lets build a json of the type,question,answers
	#so type is an array of questions, and questions has again an array of answers
	generateJsonObj = generatejson.JSONUtil()		
	jsonOp = generateJsonObj.generatejson(data,analyzeData)
	print jsonOp	

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)

