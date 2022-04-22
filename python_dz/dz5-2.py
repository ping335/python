'''
string = 'HjhfdhHbvUj'
new_string = []
for s in string:
    if s.isupper():
        new_string.append('_')
    else:
        new_string.append(s)

word = ''.join(new_string)


print(word)
'''



