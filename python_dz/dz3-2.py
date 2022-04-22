n = int(input())
even = 0
odd = 0


while n > 0:
	if n % 10 % 2 == 0:
		even = even + (n % 10)
	else:
		odd = odd + (n % 10)
	n = n//10

'''
если первое число

'''
sum = (odd) - (even)

print("сумма неч - чет = ", sum)
print("сумма нечетных цифр = ", odd)
print("сумма четных цифр = ", even)
