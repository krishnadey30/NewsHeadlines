#! /usr/bin/python
import sys
oldcategory = None
count = 0
for row in sys.stdin:
	data=row.strip().split('\t')
	if len(data)!=2:
		continue
	thiscategory,thiscount=data
	if oldcategory and oldcategory!=thiscategory:
		print "{0}\t{1}".format(oldcategory,count)
		oldcategory=thiscategory
		count=0
	oldcategory=thiscategory
	count+=1

if oldcategory!=None:
	print "{0}\t{1}".format(oldcategory,count)
