import json

class AnalyzedJson:

	style = ""
	question = ""
	answers = ""

	def __init__(self):
		return

	def __init__(self,style,question,answers):
		self.style = style
		self.question = question
		self.answers = answers

	def toJson(self):
		return json.dumps({'style':"'"+self.style+"'",'question':"'"+self.question+"'",'answers':"'"+self.answers+"'"})