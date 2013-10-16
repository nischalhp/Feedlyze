from flask import Flask
from flask import request
from flask import render_template
import readCsv

app = Flask(__name__)

@app.route('/')
def atHome():
	return render_template('index.html')

@app.route('/index.html')
def atBase():
	return render_template('index.html')

@app.route('/analyze/<path>')
def analyzeData(path):
	readCsvObj = readCsv.readCsv(path)
	data = readCsvObj.getData()
	print data


if __name__=='__main__':
	app.run(debug=True)

