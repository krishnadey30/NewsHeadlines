#! /usr/bin/python
import sys
def reducer():
	l=[]
	oldcategory = None
	count = 0
	for row in sys.stdin:
		data=row.strip().split('\t')
		if len(data)!=2:
			continue
		thiscategory,thisheadline=data
		if oldcategory and oldcategory!=thiscategory:
			print "{0}\t{1}".format(oldcategory,count)
			oldcategory=thiscategory
			count=0
			l=[]
		oldcategory=thiscategory
		count+=1
		l.append(thisheadline)

	if oldcategory!=None:
		print "{0}\t{1}".format(oldcategory,count)
def main():
	reducer()


if __name__ =="__main__": main()
