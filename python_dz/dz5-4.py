#string = 'HjhfdhHbvUj'


def camel_to_snake(name):
	snake_str = []
	for n, s in enumerate(name):
		if s.isupper():
			if n == 0:
				snake_str.append(s.lower())
			else:
				snake_str.append('_'+ s.lower())
		else:
			snake_str.append(s)
	
	word = ''.join(snake_str)
	return word

print(camel_to_snake('Etkcvc'))

def snake_to_camel(name):
	camel_str = []
	name = name.replace('', ' ').split()
	for i in range(len(name)):
		if i == 0:
			camel_str.append(name[i].upper())
			continue
		elif name[i] == '_':
			camel_str.append(name[i+1].upper())
			continue
		elif name[i-1] == '_':
			continue
		else:
			camel_str.append(name[i])
	word = ''.join(camel_str)
	return word
	
print(snake_to_camel('vg_and_lfnh'))
