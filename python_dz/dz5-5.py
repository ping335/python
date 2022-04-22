

name = "btjx_bxfk_ns_tnp_xdlm"

new_string = []
for n, s in enumerate(name):
	if s.islower():
		if n == 0:
			new_string.append(s.upper())
		else:
			new_string.append(s.lstrip('_'))
	else:
		new_string.append(s)
		
word = ''.join(new_string)
	
print(word)









