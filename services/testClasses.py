import readCsv
import analyzeData
readObj = readCsv.GetData('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
from collections import Counter
outputDictionary = readObj.getData()
analyzeObj = analyzeData.analyze(outputDictionary)
interpretation = analyzeObj.analyzeData()
for key,value in interpretation.iteritems():
	if key == 'opinion':
		for question in value:
			answers = outputDictionary[question]
			print Counter(answers)
			