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
		worksheets = gc.open_by_url(self.path)
		print worksheets
		worksheet = worksheets.get_worksheet(0)
		questions_list = worksheet.row_values(1)
		print questions_list
		# return data