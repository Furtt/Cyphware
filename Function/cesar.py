def encrypt(text,key):
	text = text.lower()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	cesared = ''.join(alphabet[(ord(i)+key-97)%26] for i in text)
	return cesared

def decrypt(text,key):
	text = text.lower()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	decesared = ''.join(alphabet[(ord(i)-key-97)%26] for i in text)
	return decesared
