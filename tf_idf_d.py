#1st make starbetutf without inrev


def tf_idf():

	import csv
	import math
	import collections
	import glob

	l=0
	wl=0
	revlist={}

	bfile=open("subrev.csv","r")
	bdata=csv.reader(bfile)
	bdata.next()
	for line in bdata:
		revlist[line[0]]=int(0)
	print revlist

	rfile=open("rev_star.csv","wb")
	rwriter=csv.writer(rfile)
	rwriter.writerow(["rev_id","star"])

	sfile=open("s_wordsum.csv","wb")
	swriter=csv.writer(sfile)
	swriter.writerow(["star","sum"])


	for num in range(1,6):
		dic=collections.OrderedDict()
		ofile=open("sbetu/star"+str(num)+".csv","wb")
		csvwriter=csv.writer(ofile)
		csvwriter.writerow(["t","n","sum","tf"])
		shoplist=glob.glob("s"+str(num)+"/*")
		#print shoplist
		for name in shoplist:
			ifile=open(name,"r")
			idata=csv.reader(ifile)
			idata.next()
			
			for line in idata:
				if((line[0] in revlist)==False):
					wordlist=line[2].split()
					for word in wordlist:
						if(str(word) in dic):
							dic[str(word)]=dic[str(word)]+1
						else:
							dic[str(word)]=1
						wl=wl+1
				else:
					print line[0],num
					rwriter.writerow([line[0],num])
			ifile.close()
		csvwriter.writerows(dic.items())	
		swriter.writerow([num,wl])
		print wl
	ofile.close()	
	bfile.close()
	rfile.close()
