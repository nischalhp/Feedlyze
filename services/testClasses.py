import readCsv
import analyzeData
from generatejson import JSONUtil
import thread



readObj = readCsv.CSVReader('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
outputDictionary = readObj.getData()
#print outputDictionary
analyzeObj = analyzeData.Analyzer(outputDictionary)

interpretation = analyzeObj.analyzeData()
for key,value in interpretation.iteritems():
    print key 


#all questions with answer have been put in their bins
# now need to run analysis on text objectsvagrant 
JSONObj = JSONUtil()

#now since we have 3 things - scale , opinion and analytics 
#i shall spawn three threads

# try:
#     thread.start_new_thread(JSONObj.generatejson, (outputDictionary,interpretation,'opinion'))


#JsonOutput = JSONObj.generateJson(outputDictionary,interpretation)
#print JSONObj
