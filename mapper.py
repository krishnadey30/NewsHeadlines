#!/usr/bin/python

import sys
import csv
import re
def mapper():
	reader=csv.reader(sys.stdin, delimiter='\t')
	for line in reader:
		date=line[0]
		category = line[1].split('.')
		headline = line[2]
		# allwords = re.findall(r"[\w']+",headline)
		# allwords = map(lambda x: x.lower(),allwords)
		for cat in category:
			print "{0}\t{1}".format(cat,headline)

def main():
	mapper()


if __name__ =="__main__": main()
