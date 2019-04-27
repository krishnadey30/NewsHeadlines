#! /usr/bin/python
import sys
import csv
def mapper():
	reader=csv.reader(sys.stdin, delimiter=',')
	headers = next(reader,None)
	for line in reader:
		if len(line)==3:
			date = line[0]
			year = date[:4]
			month = date[4:6]
			headline = line[2]
			print "{0}\t{1}".format(year,month)

def main():
	mapper()


if __name__ =="__main__": main()
