import json
#filename = 'c.json'
#jsonData = open(filename, 'r')
def webapp(data):
	z = json.loads(open("c.json", "r").read())
	h=list()
	for i in range(50):
		h.append(0)
	num = raw_input()
	for i in range(int(num)):
	    n = raw_input()
	    y.append(n)
	#print 'ARRAY: ',y
	for i in y:
		for j in z:
			for k in j[u'ingredients']:
			#if i in j[u'ingredients']:
				if i in k:
					h[j[u'id']] = h[j[u'id']]+1;
	#print h
	m = max(h)
	n = 999999
	for i in range(len(h)):
		#print h[i]
		if h[i]==m:
			print len(z[i][u'ingredients'])
			r = len(z[i][u'ingredients']) - h[i]

			if r<n:
				n=r
				pos = i
	#print z[pos]
	ing = list()
	for i in z[pos][u'ingredients']:
		ing.append(i)
	for i in y:
		if i in ing:
			ing.remove(i)
	#print ing
