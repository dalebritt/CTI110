# Program for adding and subtracting random numbers
# 11/03/2020
# CTI-110 P5HW2_MathQuiz_BrittDale
# Dale Britt
#

import random

# Function for adding random numbers
def add_numbers():
    random_number1 = random.randint(1,1000)
    random_number2 = random.randint(1,1000)
    solution = random_number1 + random_number2
    print('  ', random_number1)
    print('+ ', random_number2)
    guess = int(input('Enter answer: '))
    while guess != solution:
        if guess > solution:
            print('Sorry, guess is too high.')
            print()
            guess = int(input('Try again: '))
        elif guess < solution:
            print('Sorry, guess is too low.')
            print()
            guess = int(input('Try again: '))
    print('Congratulations!!!! Your answer is correct..')
    
# Function for subtracting random numbers
def subtract_numbers():
    random_number1 = random.randint(1,1000)
    random_number2 = random.randint(1,1000)
    solution = random_number1 - random_number2
    print('  ', random_number1)
    print('- ', random_number2)
    guess = int(input('Enter answer: '))
    while guess != solution:
        if guess > solution:
            print('Sorry, guess is too high.')
            print()
            guess = int(input('Try again: '))
        elif guess < solution:
            print('Sorry, guess is too low.')
            print()
            guess = int(input('Try again: '))
    print('Congratulations!!!! Your answer is correct..')

# Creating main menu
player_choice = True
while player_choice:
    print()
    print('MAIN MENU')
    print()
    print('-------------------------')
    print()
    print('1. Add Random Numbers')
    print('2. Subtract Random Numbers')
    print('3. Exit')
    player_choice = int(input())
    if player_choice == 1:
        add_numbers()
    elif player_choice == 2:
        subtract_numbers()
    elif player_choice == 3:
        print('Thank you for playing...')
        print('Bye!!')
        quit()
    else:
        print('Invalid input. Please enter 1, 2, or 3')
        print()
