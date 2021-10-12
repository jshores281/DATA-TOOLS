#! python 3.7.2
############################################################
# TASKS
############################################################
# ~ load data into csv from ?ext
# ~ read data out of csv to ?ext
# ~ 
#
############################################################

import csv, sys, os
import argparse, pathlib

os.system("cls")
# ask user what type of file will be loading (?ext to csv) 

parser = argparse.ArgumentParser(description='Process some DATA.', usage='data_convrt.py [txt, pdf, csv, google sheets]')

parser.add_argument('string', metavar='[STRING]', type=str, nargs='+',
                    help='Specify which type of file reading [txt, pdf, csv, google sheets]')

parser.add_argument('read', type=argparse.FileType('r'),
            		help='read command ')

#parser.add_argument( 'convert', default=sys.stdout, type=argparse.FileType('w'),help='the location where data will be written')


args = parser.parse_args()



def load_text():
	with args.read.open('r') as _READ:
		print(_READ.read())

	


def load_pdf():
	pass


def load_csv():
	pass


def load_excel():
	pass


def load_gsheets():
	pass




for string in args.string:
	if string == "txt":
		load_text()
	elif string == "pdf":
		print("ooopss need a pdf")











