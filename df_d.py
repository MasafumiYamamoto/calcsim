#for each shop

import csv
import math
import collections
import glob

def df():
	l=0

	rfile=open("rev_wordsum.csv","r")
	rdata=csv.reader(rfile)
	rdata.next()
	iglist=[]
	for line in rdata:
		iglist.append(line[0])
		

	list=collections.OrderedDict()
	for n in range(1,6):
		ifile=open("sbetu/star"+str(n)+".csv","r")
		idata=csv.reader(ifile)
		idata.next()
		for line in idata:
			if((line[0] in iglist)==False):
				if(line[0] in list):
					list[line[0]]=list[line[0]]+1
				else:
					list[line[0]]=1
		print n
	print len(list)

	outfile=open("dft_v/dt.csv","wb")
	writer=csv.writer(outfile)
	vfile=open("dft_v/dv.csv","wb")
	vwriter=csv.writer(vfile)

	writer.writerow(list.keys())
	vwriter.writerow(list.values())

	outfile.close()
	ifile.close()
	rfile.close()
