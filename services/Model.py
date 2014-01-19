import json

#need to give class right name
class Model:

	style = ""
	question = ""
	answers = ""

	def __init__(self,style,question,answers):
		self.style = style
		self.question = question
		self.answers = answers

	def toJson(self):
		return {'style':self.style,'question':self.question,'answers':self.answers}	