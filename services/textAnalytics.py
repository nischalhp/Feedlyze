from nltk.tokenize import word_tokenize,wordpunct_tokenize, sent_tokenize 
from nltk import batch_ne_chunk ,pos_tag
from textAnalyticsBase import TextAnalyticsObj
# TextAnalyzer
class TextAnalyzer:


	def performBasicAnalytics(self,outputDictionary,analyzeData):
		TA_Obj_list = []
		key = 'analytics'
		questions = analyzeData[key]
		for question in questions:
			answers = outputDictionary[question]
			print question,answers
			TAObj = self.analyzeText(answers)
			TA_Obj_list.append(TAObj)	
			#print TAObj.sentences,TAObj.tokens,TAObj.postags,TAObj.chunks
		# 	analyzedJson = getAnalyzedJson.AnalyzedJson(key,question,dict_of_answers) 	
		# 	analyzedJson = analyzedJson.toJson()
		# 	#print analyzedJson
		# 	inner_json_list.append(analyzedJson)
		# inner_json = json.dumps({'data':inner_json_dict})	
		return TA_Obj_list

	def analyzeText(self,answers):
		#does tokenization , pos tagging , chunking and returns all 3 of them
		
		for answer in answers:
			if answer != '':
				#print answer
				#sentence tokenzier
				sentences = sent_tokenize(answer)
				# word tokenizer
				tokens = [word_tokenize(sentence) for sentence in sentences]
				#pos tagger
				postags = [pos_tag(token) for token in tokens]
				#chunking
				chunks = batch_ne_chunk(postags,binary=True)
				TAObj = TextAnalyticsObj(sentences,tokens,postags,chunks)
				return TAObj
				#print type(chunks),"chunks type"




