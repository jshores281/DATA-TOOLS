####################################################################################
####################################################################################
# xtrk_CSV - extract data from any csv based off columns and rows
####################################################################################
# TASKS
####################################################################################
# [X] - check file extension if in accepted list
# [X] - read columns in csv
# [X] - iterate over rows of specific columns
# 
# [ ] - find duplicates in rowXcolumn
# [ ] - correlate data between different columns on same rows 
####################################################################################


# extract data from any spread-sheet (csv,xls,google-sheets) based off columns and rows

import csv, os, sys
import pandas as pd

# acceptable file formats
ACC_XTNS = ["csv","xls","xlsx","odt"]
os.system('cls')
os.system('title ~~SPREADSHEET EXTRACT~~')
print("~~DATA EXTRACT~~")



#######################################################################################
# DRAG AND DROP CSV HERE
def file_path():
	print(f"\nACCEPTABLE FILE FORMATS = {ACC_XTNS}")
	file_path.RAW_PATH = input(f"DRAG AND DROP {ACC_XTNS} FILE HERE: ")

	# FORMAT PATH (CONVERT / TO \, REMOVES ' ', GETS CSV NAME)
	file_path.RAW_PATH = file_path.RAW_PATH.replace("\\", "/")
	file_path.RAW_PATH = file_path.RAW_PATH.strip('""')
	file_path.FILENAME = file_path.RAW_PATH.rsplit('/',1)[-1]

	# CHECKS IF FILE IS CSV
	file_path.FILENAMEX = file_path.FILENAME.rsplit('.',1)[-1]
	print(f"\n~FILE NAME = {file_path.FILENAME}\n~FILE EXTENSION = {file_path.FILENAMEX}\n~FILE PATHWAY = {file_path.RAW_PATH}\n")

file_path()



#for xtns in ACC_XTNS:
#	print(xtns)



#######################################################################################


def csv_read():
	try:
		with open(file_path.RAW_PATH) as rcsv:
			email_reader = csv.reader(rcsv, delimiter=',')
			csv_read.colxrow = list(email_reader)
			columns = []
			for rows in csv_read.colxrow:
				columns.append(rows)
			file_path.column = columns[0]
			print(f"\n~COLUMN NAMES = {file_path.column}\n")
			for col_nums in enumerate(file_path.column):
				print(col_nums)
	except FileNotFoundError:
		input("FILE NOT FOUND. PRESS [ENTER]: ")
		sys.exit()


	def col_pick():
		COLUMN_DROP = input("\nTYPE COLUMN NUMBER TO SEARCH FOR ROWS: ")
		COLUMN_DROP = COLUMN_DROP.split(",")

		for colnums in COLUMN_DROP:
			sel_cols = file_path.column[int(colnums)]
			#sel_cols = sel_cols.split()
			print(sel_cols)
			

		print("\nCOLUMNS CHOOSEN: %s\nCOLUMN NUMBERS: %s\n" % (sel_cols, COLUMN_DROP))

		col_nums = len(COLUMN_DROP)
		print(col_nums)
		for rows in csv_read.colxrow[1:]:
			for cols in COLUMN_DROP:
				#print(file_path.column[int(cols)]) # LABELS COLUMNS SELECTED AND PRINTED
				rxc = rows[int(cols)]
				rxc = rxc.split(' ')
				print(rxc)
				for a in rxc:
					print(a, "\n")
					#print(b, "\n")
		#splitter = rxc[::col_nums]
		#print(splitter)
				#print(rows[int(cols)])	
				#trp_dict = dict(zip(rows,rows[int(cols)]))
				#print(trp_dict)
		return csv_read()
		"""
		try:
		
		except (ValueError, IndexError):
			#del (file_path.RAW_PATH, file_path.FILENAMEX, file_path.FILENAME)
			#file_path()
			input(f"ACCEPTS ONLY NUMBERS 0 - {len(file_path.column)-1} PRESS [ENTER]: ")
			sys.exit()
		"""	
	col_pick()

	def col_xprt():
		pass






#######################################################################################

def panda_csv():
	#print("\nTHIS WILL READ EXCEL && CSV FILES LATER")
	#print(f"\n~FILE NAME = {file_path.FILENAME}\n~FILE EXTENSION = {file_path.FILENAMEX}\n~FILE PATHWAY = {file_path.RAW_PATH}\n")
	panda_csv.df = pd.read_csv(file_path.RAW_PATH)
	print(panda_csv.df)

	#select_cols = input("\nselect columns to read out: ")
	#scols = select_cols.split(",")
	#print(scols)
	#for col in scols:
	#	print(panda_csv.df[col])

	print("\n1. Export Columns","\n2. MAIN-MENU")
	read_mthd = input(str("CHOOSE OPTIONS: "))
	if read_mthd == "1":
		return csv_read()
	if read_mthd == "2":
		return xtns_chk()





#######################################################################################

def xls_read():
	print("THIS WILL READ EXCEL FILES LATER")
	print(f"\n~FILE NAME = {file_path.FILENAME}\n~FILE EXTENSION = {file_path.FILENAMEX}\n~FILE PATHWAY = {file_path.RAW_PATH}\n")









#######################################################################################

def xtns_chk():
	if file_path.FILENAMEX not in ACC_XTNS:
		print(f"FAILED! FILE EXTENSION: [{file_path.FILENAMEX}] IS NOT ACCEPTED! \n{ACC_XTNS} \n~~EXITTING!")
		sys.exit()
	if file_path.FILENAMEX in ACC_XTNS:
		print(f"SUCCESS! FILE EXTENSION: [{file_path.FILENAMEX}] IS ACCEPTED! \n{ACC_XTNS}")
		if file_path.FILENAMEX == "csv":
			return panda_csv()
		if file_path.FILENAMEX in ACC_XTNS:
			print(f"\nTHIS IS A {file_path.FILENAMEX} FILE")
			return xls_read()


xtns_chk()





#######################################################################################
#######################################################################################

