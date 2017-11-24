

flines = open('TheVictors.txt')
counts = dict()
for line in flines:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0)+1
lst = []
for key,val in counts.items():
	newtup = (val,key)
	lst.append(newtup)
lst = sorted(lst, reverse=True)
for val,key in lst[:15]:
	print(key,val)
