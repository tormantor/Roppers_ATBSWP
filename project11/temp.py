import random as r
guess=''
while guess not in (1,0):
	print('Guess the coin toss! Enter heads or tails: ')
	guess=int(input())
	toss=r.randint(0,1)
	if toss==guess:
		print('You got it!')
	else:
		print('Nope! Guess again!')
		guess=int(input())
		if toss==guess:
			print('You got it')
		else:
			print('Nope. You are really bad at this game')		
	
