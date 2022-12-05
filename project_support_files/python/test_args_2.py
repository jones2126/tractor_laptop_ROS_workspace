#!/usr/bin/python3
# reference: https://www.tutorialspoint.com/python3/python_tutorial.pdf  page 34/512
# usage: test_args_2.py <inputfile> 
#
import sys
def main(argv):
	inputfile = ''
	inputfile = argv
	print ("Input file is:", inputfile)
if __name__ == "__main__":
	main(sys.argv[1])
	print ("EOJ")