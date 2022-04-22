print('hii')


#из CamelCase в snake_case
def camel_snake(str_name):
	str_name.replace(([a-z][A-Z]+)|([A-Z]+[a-z]), '\L$1')
	return str_name
	

#из snake_case  в CamelCase
def snake_camel(str_name):
	str_name.replace('\L$1', ([a-z][A-Z]+)|([A-Z]+[a-z]))
	return str_name

#поиск и замена строки
#поиск строки
welcome = "Hello world! Goodbye world!"
index = welcome.find("wor")
print(index)   

phone = "+1-234-567-89-10"
edited_phone = phone.replace("-", " ")
print(edited_phone)     # +1 234 567 89 10  


print('-------------')
#найти
'''
вот у нас есть строка
и нам нужно вней найти большие буквы
и вывести их на экран



HjhfdhHbvUj
hjhfdh_hbv_j
'''

stroka = "IsmogiVse"
indexx = stroka.find("V")
#заменить эту букву на v маленькое
editstr = stroka.replace(([a-z][A-Z]+)|([A-Z]+[a-z]), '\L$1')
print(editstr)

print(indexx)

	
	


