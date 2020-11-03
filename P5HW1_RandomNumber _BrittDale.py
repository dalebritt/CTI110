# Random number game
# 11/02/2020
# CTI-110 P5HW1 - Random Number
# Dale Britt
#

import random

# Main number game function that takes user input guesses
def number_game():
    random_number = random.randint(1,100)
    guess = int(input('Enter a number between 1 and 100: '))
    while guess != random_number:
        if guess > random_number:
            print('Too high, try again')
            guess = int(input('Enter a number between 1 and 100: '))
        elif guess < random_number:
            print('Too low, try again')
            guess = int(input('Enter a number between 1 and 100: ')) 
    print('Congratulations!!!')
    play_again = int(input('Would you like to play again? (1 - yes, 2 - no)'))
    if play_again == 1:
        player_choice = True
    elif play_again == 2:
        quit()
    else:
        print('Invalid input. Please enter 1 or 2')
        print()
        
# Creating main menu
player_choice = True
while player_choice:
    print()
    print('MAIN MENU')
    print()
    print('-------------------------')
    print()
    print('1) Play Game')
    print('2) Exit')
    player_choice = int(input())
    if player_choice == 1:
        number_game()
    elif player_choice == 2:
        quit()
    else:
        print('Invalid input. Please enter 1 or 2')
        print()



