from nltk.tokenize import word_tokenize,wordpunct_tokenize, sent_tokenize 
from nltk import batch_ne_chunk ,pos_tag

# TextAnalyzer
class TextAnalyzer:


	def __init__(self):
		self.entities = []

	def extractEntities(self,tree):
		if hasattr(tree, 'node') and tree.node:
			#print tree.node,"tree node"
			if tree.node == 'NE':
				for child in tree:
					self.entities.append(' '.join([child[0] for child in tree]))
					#print child,"child"
			else:
				for child in tree:
					#print child,"recursive child"
					self.extractEntities(child)


	def analyzeText(self,answers):
		#find entities and TFIDF for each answers and then add it up in the end
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
				#find entites
				entites = []
				for tree in chunks:
					#print tree,"tree"
					self.extractEntities(tree)
				
				#print self.entities
				





