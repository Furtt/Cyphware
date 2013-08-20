from itertools import izip
def encrypt(text):
	text.lower()
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	reverseAlphabet = 'zyxwvutsrqponmlkjihgfedcba'
	i=0
	j=0
	reversedText = ''
	while i<len(text):
		while j<len(alphabet):
			if text[i] == alphabet[j]:
				reversedText = reversedText + reverseAlphabet[j]
			j+=1
		i+=1
		j=0
	#~ reversedText = ''.join(j for (i,j) in izip(alphabet, reverseAlphabet)) #if i==j ternary condition
	return reversedText
	
	#The encrypt function can be improve
