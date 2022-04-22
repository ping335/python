
'''
берем строку
и если первая буква в верхнем регистре то переводим ее в нижний
name = "GoiiYew"
name = name[:1].lower() + name[1:]
print(name)
'''

string = 'HjhfdhHbvUj'


new_string = []
for n, s in enumerate(string):
	if s.isupper():
		if n == 0:
			new_string.append(s.lower())
		else:
			new_string.append('_'+ s.lower())
	else:
		new_string.append(s)

word = ''.join(new_string)


print(word)


print('--------------')

stroka = "Vasya"

for i in enumerate(stroka):
	print(i)

a = [10, 20, 30, 40]

for id, item in enumerate(a):
	a[id] = item + 5

print(a)


print('--------------')






