import readCsv
import analyzeData

readObj = readCsv.CSVReader('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
outputDictionary = readObj.getData()
#print outputDictionary
analyzeObj = analyzeData.Analyzer(outputDictionary)
interpretation = analyzeObj.analyzeData()