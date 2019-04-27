#! /usr/bin/python
import sys
def reducer():
	l={}
	oldmonth = None
	count = 0
	for row in sys.stdin:
		data=row.strip().split('\t')
		if len(data)!=3:
			continue
		thismonth,thiscategory,thisheadline=data
		thismonth = int(thismonth)
		if oldmonth and oldmonth!=thismonth:
			for key in l.keys():
				print "{0}\t{1}\t{2}".format(oldmonth,key,l[key])
			oldmonth=thismonth
			l={}
		oldmonth=thismonth
		if thiscategory in l:
			l[thiscategory]+=1
		else:
			l[thiscategory]=1

	if oldmonth!=None:
		for key in l.keys():
			print "{0}\t{1}\t{2}".format(oldmonth,key,l[key])
def main():
	reducer()


if __name__ =="__main__": main()
