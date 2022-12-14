#!/usr/bin/python3
# reference: https://www.tutorialspoint.com/python3/python_tutorial.pdf  page 34/512
# usage: test.py -i <inputfile> -o <outputfile>
#
import sys, getopt
def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print ('errror - test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('help format - test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print ("Input file is:", inputfile)
	print ("Output file is:", outputfile)
if __name__ == "__main__":
	main(sys.argv[1:])