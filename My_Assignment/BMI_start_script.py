import argparse
import os
from BMI_calculation import find_BMI
import json

parser = argparse.ArgumentParser()

# Reading inputs from command Line

parser._optionals.title = 'List of arguments is as follow : '

parser.add_argument("-j",required=True,
	help = "Name of the input json file/Path of input json file(Compulsary Argument)")
	#type=argparse.FileType('r'))

parser.add_argument("-t",required=True,help = "Name of the input table/Path of input table(Compulsary Argument)")

parser.add_argument("-o",required=True,help = "Name of the output directory/Path of output directory(Compulsary Argument)")


args = parser.parse_args()



if not(os.path.exists(args.j)): # if input file does not exist the print the error message and exit from code.
	
	print("File does not exist. Give correct file name/file path.")
	exit()
elif not(os.path.exists(args.t)): # if input file does not exist the print the error message and exit from code.
	
	print("Table does not exist. Give correct Table name/Table path.")
	exit()

if os.path.exists(args.o):

	print("Directory already exist, give another name for directory.")
	exit()
else:
	os.mkdir(args.o)


find_BMI(args.j, args.t, args.o)