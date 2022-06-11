import random
start = input('please input a number as the start of the range for your coming guesses: ')
end = input('please input a number as the end of the range for your coming guesses: ')
start = int(start)
end = int(end)

while end < start + 10:
	print('you cannot input the end number that is smaller than start number, please input a number that is at least 10 larger than your start number ')
	end = input('please input a number as the end of the range for your coming guesses: ')
	end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1 # count = count + 1
	num = input('please guess a number between your preset range: ')
	num = int(num)
	if num == r:
		print('Bingo! congratulation!')
		print('it is your #', count, 'guess')
		break;
	elif num > r:
		print('your guess is larger than the random number')
	elif num < r:
		print('your guess is smaller than the random number')
	print('it is your #', count, 'guess')



