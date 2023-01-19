#! python 3.7.2
############################################################
# TASKS
############################################################
# ~ load data into csv from ?ext
# ~ read data out of csv to ?ext
############################################################

import csv, sys, os
import argparse

os.system("cls")
# ask user what type of file will be loading (?ext to csv) 
parser = argparse.ArgumentParser('help', 
								description='Process some DATA.', 
								usage='data_convrt.py [txt, pdf, csv, google sheets]')

parser.add_argument('string', 
					metavar='[STRING]', 
					type=str, 
					nargs='+', 
					help='Specify which type of file reading.')

parser.add_argument('FILE', 
					metavar='[FILE-PATH]',
					type=argparse.FileType('r'), 
					help='Path to file or file if in directory')


#parser.add_argument('write', type=argparse.FileType('w'), help='write command of specified file.')
#parser.add_argument( 'convert', default=sys.stdout, type=argparse.FileType('w'),help='the location where data will be written')

args = parser.parse_args()

def load_text():
	with args.FILE as _READ:
		print(_READ.read())
		sys.exit()

def load_pdf():
	print("ooopss need a pdf")
	sys.exit()

def load_csv():
	pass

def load_excel():
	pass

def load_gsheets():
	pass


string_list = ["txt", "pdf", "csv", "gsheets"]

for string in args.string:
	if string == "txt":
		load_text()
	elif string == "pdf":
		load_pdf()
	elif string == "csv":
		load_csv()
	

for sl in string_list:
	if string not in sl:
		print("command not found")
		parser.print_help()
		break

