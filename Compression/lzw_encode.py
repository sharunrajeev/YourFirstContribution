table = dict()

for i in range(256):
	table[chr(i)] = str(i)

count = 255


def lzw_encode(s):
	i = 0
	if not len(s):
		return
		
	ret = ""
	global count
	p = s[0]
	
	while i < (len(s)-1):
		c = s[i+1]
		
		if p+c in table.keys():
			p = p+c
			
		else:
			ret =ret+' '+table[p]
			count += 1
			table[p+c] = str(count)
			p = c
		
		i += 1
	
	ret = ret+' '+table[p]
	return ret
print("Enter the text to be encoded:")
print(lzw_encode(input()))
