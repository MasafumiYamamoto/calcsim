
#for each review,make BoW


def revtfidf():

	import csv
	import collections



	wl=0
	bfile=open("subrev.csv","r")
	bdata=csv.reader(bfile)
	bdata.next()
	wfile=open("rev_wordsum.csv","wb")
	write=csv.writer(wfile)
	write.writerow(["rev_id","sum"])

	for line in bdata:
		dic=collections.OrderedDict()
		wordlist=line[2].split()
		for word in wordlist:
			if(str(word) in dic):
				dic[str(word)]=dic[str(word)]+1
			else:
				dic[str(word)]=1
			wl=wl+1
				
		ofile=open("rev/"+line[0]+".csv","wb")
		oriter=csv.writer(ofile)
		oriter.writerow(["t","n","sum","tf"])
		oriter.writerows(dic.items())
		write.writerow([line[0],wl])

	bfile.close()
	wfile.close()
