import csv
import gspread

class GetData:
	
	path = ""

	def __init__(self):
		return


	def __init__(self,path):
		self.path = path

	def helloWorl():
		print "hello"


	def getData(self):
		# need to read email and pass from a cnfig later
		gc = gspread.login('analyzedatum@gmail.com','mynameisanalyzedatum')
		print gc
		# worksheets = gc.open_by_url(self.path)
		# worksheet = worksheets.get_worksheet(0)
		# questions_list = worksheet.row_values(0)
		# print questions_list
		# return data