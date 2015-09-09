#for each review calc simirality

def calcp():
	import csv
	import math
	import collections
	import glob
	import numpy


	i1file=open("dft_v/dt.csv","r")
	i1data=csv.reader(i1file)
	i2file=open("dft_v/dv.csv","r")
	i2data=csv.reader(i2file)
	dflist=collections.OrderedDict()

	for line in i1data:
		for num in range(0,len(line)):
			dflist[line[num]]=0
	k=dflist.keys()
	for line in i2data:
		for num in range(0,len(line)):
			dflist[k[num]]=line[num]
			
	print "copy"

	#print dflist

	rfile=open("rev_wordsum.csv","r")
	rdata=csv.reader(rfile)
	rdata.next()
	rdic={}
	for line in rdata:
		rdic[line[0]]=int(line[1])
	sfile=open("s_wordsum.csv","r")
	sdata=csv.reader(sfile)
	sdata.next()
	sdic={}
	for line in sdata:
		sdic[line[0]]=int(line[1])

	#print rdic
	#print sdic

	rsfile=open("rev_star.csv","r")
	rsdata=csv.reader(rsfile)
	rsdata.next()
	rslist={}
	for line in rsdata:
		rslist[line[0]]=int(line[1])


	#infile...rev & referedfile  output...probability of refered

	reviewlist=glob.glob("rev/*")
	for reviewname in reviewlist:
		outfile=open("result/"+reviewname,"wb")
		outwriter=csv.writer(outfile)
		outwriter.writerow(["revid","aite","sim","seikai"])
		
		
		######		calc mine tfidf
		wordlist=collections.OrderedDict()
		revfile=open(reviewname,"r")
		revdata=csv.reader(revfile)
		revdata.next()
		for line in revdata:
			######  	calc tf*idf 
			if(line[0] in dflist):
				wordlist[line[0]]=float(line[1])/int(rdic[reviewname[4:-4]])*(math.log10(5.0/float(dflist[line[0]]))+1)
			
		#|review|
		reviewlen =numpy.linalg.norm(wordlist.values())
		print reviewlen
		
		######		calc each star tfidf
		for num in range(1,6):
			reffile=open("sbetu/star"+str(num)+".csv")
			refdata=csv.reader(reffile)
			refdata.next()
			shopwordlist=collections.OrderedDict()
			for line in refdata:
				if(line[0] in dflist):
					shopwordlist[line[0]]=float(line[1])/sdic[str(num)]*(math.log10(5.0/float(dflist[line[0]]))+1)
			
			####|star|
			shoplen=numpy.linalg.norm(shopwordlist.values())
			#print shoplen
			
			#calc dis
			score=0
			for word in wordlist.keys():
				if(word in shopwordlist.keys()):
					score=score+wordlist[word]*shopwordlist[word]
			if(reviewname[4:-4] in rslist):
				outwriter.writerow([reviewname[4:-4],num,score/shoplen/reviewlen,rslist[reviewname[4:-4]]])
			else:
				outwriter.writerow([reviewname[4:-4],num,score/shoplen/reviewlen,-1])
		print reviewname[4:-4]

	outfile.close()
	reffile.close()
	revfile.close()
	i1file.close()
	i2file.close()
	sfile.close()
	rfile.close()
