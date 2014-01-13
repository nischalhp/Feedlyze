import readCsv
import analyzeData
from generatejson import JSONUtil
readObj = readCsv.CSVReader('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
outputDictionary = readObj.getData()
#print outputDictionary
analyzeObj = analyzeData.Analyzer(outputDictionary)
interpretation = analyzeObj.analyzeData()
#all questions with answer have been put in their bins
# now need to run analysis on text objects
JSONObj = JSONUtil()
JsonOutput = JSONObj.generateJson(outputDictionary,interpretation)
print JSONObj
