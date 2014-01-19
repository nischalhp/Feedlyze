import re

#refactor the class name to Analyzer
class Analyzer:

	excel_dictionary = {}
	output_obj = {}


	def __init__(self,dictionary):
		self.excel_dictionary = dictionary
		self.output_obj = {}

	def analyzeData(self):
		# analyze the data and group them into different parts
		# example , opinion usually have just yes , no , maybe
		# other items which have string data , we can perform text analytics on them
		# if it is just dates , we can check activity
		# depending on the question itself we can check what kind of output they are looking for
		# v1 - only get opinion poll and perform some basic text analytics
		interpretation = {}
		for key,value in self.excel_dictionary.iteritems():
			#empty list check
			#print key,value
			if all(word == '' for word in value):
				style = 'none'
				# assuming that same questions are not repeated
				if style in interpretation.keys():
					list_styles = []
					list_styles = interpretation[style]
					list_styles.append(key)
					del interpretation[style]
					interpretation[style] = list_styles
				else:
					list_styles = []
					list_styles.append(key)
					interpretation[style] = list_styles
			#
			#if all(word == 'YES' or word == 'NO' or word == 'MAYBE' for len(word) in value):
			
			# assuming opinions have just one word
			# can take the length parameter to be dynamic
			# the funny part here is opinion can we words or sometimes on a scale of 1 to 10 types
			# so need to distinguish these two
			max_length = 0
			for word in value:
				word_length = len(re.findall(r'\w+',word))
				if word_length > max_length:
					max_length = word_length
			# here if the length is one i check between scale or opinion
			# scale will have everything as numbers so this is useful to us
			if max_length == 1 :
				if all(re.match('\d+',word) or word == '' for word in value):
					style = 'scale'
					#assuming that same questions are not repeated
					if style in interpretation.keys():
						list_styles = []
						list_styles = interpretation[style]
						list_styles.append(key)
						del interpretation[style]
						interpretation[style] = list_styles
					else:
						list_styles = []
						list_styles.append(key)
						interpretation[style] = list_styles
					# print key,value,"scale"
				else:
					style = 'opinion'
					#assuming that same questions are not repeated
					if style in interpretation.keys():
						list_styles = []
						list_styles = interpretation[style]
						list_styles.append(key)
						del interpretation[style]
						interpretation[style] = list_styles
					else:
						list_styles = []
						list_styles.append(key)
						interpretation[style] = list_styles
					# print key,value,"opinion"

			# for those which require some basic text analytics to be done
			if max_length > 1:
				#print value
				if all(re.match('^[0-9a-zA-Z].*$',word) or word == '' for word in value):
					#its an actual string and not some number like date
					# it may so happen the reponse that is a bigger string is actually a repetitive response which can go in again as opinion 
					# assuming that in a size of 10 elements in a list , only 2 strings are used 10 times then its basically a poll
					#print key,value,"analytics"
					list_without_nulls = [x for x in value if x != '']
					size_of_list = len(list_without_nulls)
					unique_list = list(set(list_without_nulls))
					size_of_unique_list = len(unique_list)
					#print size_of_unique_list,size_of_list,value
					#print list_without_nulls,size_of_list,unique_list,size_of_unique_list
					if size_of_unique_list <= 3 and size_of_list > 3:
						#basically this a poll again
						#print list_without_nulls,key,"opinion+analytics"
						style = 'opinion'
						#assuming that same questions are not repeated
						if style in interpretation.keys():
							list_styles = []
							list_styles = interpretation[style]
							list_styles.append(key)
							del interpretation[style]
							interpretation[style] = list_styles
						else:
							list_styles = []
							list_styles.append(key)
							interpretation[style] = list_styles
					else:
						style = 'analytics'
						if style in interpretation.keys():
							list_styles = []
							list_styles = interpretation[style]
							list_styles.append(key)
							del interpretation[style]
							interpretation[style] = list_styles
						else:
							list_styles = []
							list_styles.append(key)
							interpretation[style] = list_styles

		#return output
		# for key,value in interpretation.iteritems():
		#  	print key,value
		return interpretation

		