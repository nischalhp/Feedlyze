import readCsv
import analyzeData
readObj = readCsv.GetData('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
outputDictionary = readObj.getData()
analyzeObj = analyzeData.analyze(outputDictionary)
analyzeObj.analyzeData()