#! /usr/bin/python
import sys
import csv
import re
def mapper():
	reader=csv.reader(sys.stdin, delimiter=',')
	headers = next(reader,None)
	for line in reader:
		if len(line)==3:
			date = line[0]
			year = date[:4]
			month = date[4:6]
			category = line[1].split('.')
			headline = line[2]
			# allwords = re.findall(r"[\w']+",headline)
			# allwords = map(lambda x: x.lower(),allwords)
			for cat in category:
				print "{0}\t{1}\t{2}".format(month,cat,headline)

def main():
	mapper()


if __name__ =="__main__": main()
