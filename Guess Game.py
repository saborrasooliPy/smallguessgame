secret_number = 4
guess_count = 0
guess_limit = 2
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count  += 1
    if guess == secret_number:
        print('You Won The iphone 45')
        break
else:
    print('Sorry, You Faild')