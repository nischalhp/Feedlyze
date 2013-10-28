import csv
import gspread 
class GetData:
	
	path = ""

	def __init__(self):
		return


	def __init__(self,path):
		self.path = path



	def getData(self):
		# need to read email and pass from a cnfig later
		gc = gspread.login('analyzedatum@gmail.com','mynameisanalyzedatum')
		
		# gets worksheets
		worksheets = gc.open_by_url(self.path)
		
		#gets the required sheet
		worksheet = worksheets.get_worksheet(0)
		
		#returns all the records with their questions as list of dictionaries
		list_of_dictionary = worksheet.get_all_records(empty2zero=False)
		
		#dictonary that holds data of each questions and all their answers
		question_answers = {}
		
		for dictionary in list_of_dictionary:
			for key in dictionary.keys():
				#print key,dictionary[key]
				if key in question_answers.keys():
					#if it exists then append the data
					values = question_answers[key]
					values.append(str(dictionary[key]).upper())
					del question_answers[key]
					question_answers[key] = values
				else:
					#if key does not exits create the key
					values = []
					value = str(dictionary[key]).upper()
					values.append(value)
					question_answers[key] = values

		# for key,value in question_answers.iteritems():
		# 	print key,value

		return question_answers	
