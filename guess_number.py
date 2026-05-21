import random

random_num = random.randint(1, 50)
player_guess = ''

print(' Number Guessing Game '.center(40, '*'))
print('You have 5 tries to get the answer.')
print('Guess the number from 1 to 50.')

for i in range(5):
    try:
        player_guess = int(input('Guess the number: '))

        if player_guess < random_num:
            print('Wrong: The answer is greater than', player_guess)
        elif player_guess > random_num:
            print('Wrong: The answer is less than', player_guess)
        elif player_guess == random_num:
            print('Correct! You got the right answer in ' + str(i + 1) + ' tries')
            break
    except ValueError:
        print('Invalid input! Input only integers.')
if player_guess != random_num:
    print('Sorry! The answer is', random_num)

