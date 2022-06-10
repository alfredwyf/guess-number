import random

r = random.randint(1, 100)
while True:
	num = input('please guess a number: ')
	num = int(num)
	if num == r:
		print('you are correct! congratulation!')
		break;
	elif num > r:
		print('your guess is larger than the actual')
	elif num < r:
		print('your guess is smaller than the actual')



