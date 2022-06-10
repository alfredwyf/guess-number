import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('please guess a number between 1-100: ')
	num = int(num)
	if num == r:
		print('Bingo! congratulation!')
		print('it is your', count, 'guess')
		break;
	elif num > r:
		print('your guess is larger than the random number')
	elif num < r:
		print('your guess is smaller than the random number')
	print('it is your', count, 'guess')



