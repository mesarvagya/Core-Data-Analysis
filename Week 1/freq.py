import sys, getopt
import argparse
__author__ = "Sarvagya Pant"
def main():
	"""
	Calculates the effective count of specific text from file.
	Usage:
	python freq.py --help for getting more information
	python freq.py --file data.txt to get the output
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--file", help="Enter File Name")
	args = parser.parse_args()
	try:
		filename = args.file
		print get_count(filename)
	except NameError:
		print "Please use python freq.py --file <filename> or check python freq.py --help"
	
def get_count(filename):
	count = {}
	f = open(filename,"r")
	all_data = []
	for item in f.readlines():
		temp = []
		for data in item.split():		
			temp.append(data)
		all_data.append(temp)

	for data in all_data:
		count[data[-1]] = count.get(data[-1],0)+1

	f.close() 
	return count
if __name__ == "__main__":
	main()