#! /usr/bin/python
import sys
def reducer():
	oldyear = None
	count = 0
	l = [0]*12
	for row in sys.stdin:
		data=row.strip().split('\t')
		if len(data)!=2:
			continue
		thisyear,thismonth=data
		thisyear = int(thisyear)
		thismonth = int(thismonth)
		if oldyear and oldyear!=thisyear:
			for i in range(12):
				print "{0}\t{1}\t{2}".format(oldyear,i+1,l[i])
			oldyear=thisyear
			l=[0]*12
		oldyear=thisyear
		l[thismonth-1]+=1

	if oldyear!=None:
		for i in range(12):
			print "{0}\t{1}\t{2}".format(oldyear,i+1,l[i])
def main():
	reducer()


if __name__ =="__main__": main()
