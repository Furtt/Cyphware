from itertools import izip, cycle

def encrypt(text, key):
	text = text.lower()
	key = key.lower()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	vigenered = ''.join(alphabet[(ord(i)+ord(j)-2*97)%26] for (i,j) in izip(text, cycle(key)))
	return vigenered
	

def decrypt(text, key):
	text = text.lower()
	key = key.lower()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	devigenered = ''.join(alphabet[(ord(i)-ord(j))%26] for (i,j) in izip(text, cycle(key)))
	return vigenered
