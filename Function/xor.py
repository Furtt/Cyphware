#Code from https://gist.github.com/revolunet/2412240
from itertools import izip, cycle
import base64

# a	b	=
# 0 0	0
# 0 1	1
# 1 0	1
# 1 1	0
 
def encrypt(data, key):		
	if encode == False:
		data = base64.decodestring(data)
	xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
	return base64.encodestring(xored).strip()

def decrypt(data, key):		
	if encode == False:
		data = base64.decodestring(data)
	dexored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
	return xored

	
#How to improve : chose if ascii or binary that come in.
