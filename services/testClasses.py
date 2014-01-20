import readCsv
from RuleEngine import Analyzer
from generatejson import JSONUtil
import thread
from textAnalytics import TextAnalyzer
from entityExtraction import EntityExtractor


readObj = readCsv.CSVReader('https://docs.google.com/spreadsheet/ccc?key=0AiNZkDgFRjjOdERzLU01NTdVeE5ZaDUzbi1xNTRfSnc&usp=sharing#gid=0')
outputDictionary = readObj.getData()
#print outputDictionary
Analyzer = Analyzer(outputDictionary)

interpretation = Analyzer.analyzeData()

#all questions with answer have been put in their bins
# now need to run analysis on text objectsvagrant 

JSONObj = JSONUtil()
#now since we have 3 things - scale , opinion and analytics 
JsonOutputOpinion = JSONObj.generateJson(outputDictionary,interpretation,'opinion')
print JsonOutputOpinion
JsonOutputScale = JSONObj.generateJson(outputDictionary,interpretation,'scale')
print JsonOutputScale
TextAnalyticsObj = TextAnalyzer()
TAObjList = TextAnalyticsObj.performBasicAnalytics(outputDictionary,interpretation)
#entityExtractor
for TAObj in TAObjList:
    entityObj = EntityExtractor(TAObj.chunks)
    entityObj.entityExtraction()
    #print entityObj
    #print JSONObj
