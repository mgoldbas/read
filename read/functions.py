import string, re


def chunks(text):#hand it the text, it hands back the proper number of Sentence classes
	n = 100 #number of sentences per element
	periods = text.count('.') 	#count the number of sentences to see if it needs to be broken in to chunks 
	exclaimations = text.count('!')
	questions = text.count('?')
	length = len(text)
	ends = periods + exclaimations + questions #total clauses in text
	m = []
	position = 0
	if n < ends:
		#chop up text into sentences
		while position < length: #separate all sentences by question, exclaimation or question mark
			p = string.find(text,'.',position)
			e = string.find(text,'!',position)
			q = string.find(text,'?',position)
			if p == -1:
				p = length
			if e == -1:
				e = length
			if q == -1:
				q = length		
			past = position
			low = min([p,e,q])+1
			position = low
			chunk = text[past:position]
			m.append(chunk)
		r = []
		for i in xrange(0,len(m),n):
			block = m[i:i+n]
			r.append(' '.join(block))
		return r
	else:
		return [text]

		
k = "she. is. so. very. fat. "
print chunks(k)