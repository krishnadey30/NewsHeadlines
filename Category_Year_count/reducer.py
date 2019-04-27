#! /usr/bin/python
import sys
def reducer():
	l={}
	oldyear = None
	count = 0
	for row in sys.stdin:
		data=row.strip().split('\t')
		if len(data)!=3:
			continue
		thisyear,thiscategory,thisheadline=data
		thisyear = int(thisyear)
		if oldyear and oldyear!=thisyear:
			for key in l.keys():
				print "{0}\t{1}\t{2}".format(oldyear,key,l[key])
			oldyear=thisyear
			l={}
		oldyear=thisyear
		if thiscategory in l:
			l[thiscategory]+=1
		else:
			l[thiscategory]=1

	if oldyear!=None:
		for key in l.keys():
			print "{0}\t{1}\t{2}".format(oldyear,key,l[key])
def main():
	reducer()


if __name__ =="__main__": main()
