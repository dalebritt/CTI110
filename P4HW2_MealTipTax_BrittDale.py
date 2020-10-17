# A program for calculating meal tip tax
# 10/16/2020
# CTI-110 P3HW2 - Meal Tip Tax Calculator
# Dale Britt
#
# Set tax
tax_percentage = 6.0
user_input = 'y'
# Ask user for meal price
food_cost = int(input('Enter meal price: '))
print()
# Ask user for tip
tip_percentage = int(input('Enter Tip (16, 18, or 20): '))
while user_input != 'n':
    if tip_percentage in (16, 18, 20):
        # Output of users calculated tip and tax percentage
        print('Calculated Tip: {:.1f}'.format(tip_percentage))
        print('Calculated Tax: {:.1f}'.format(tax_percentage))
        # Total meal cost including tip and tax
        total_cost = food_cost + tip_percentage + tax_percentage
        print('Total cost including tip and tax: {:.1f}'.format(total_cost))
        print()
        user_input = input('Do you want to calculate a different tip? (y/n) ')
        if user_input in ('y', 'n'):
            if user_input == 'y':
                tip_percentage = int(input('Enter Tip (16, 18, or 20): '))
        else:
            print('Invalid input. Please enter y or n')
    else:
        # Error if tip amount out of requested input
        print('Incorrect tip Entered!!!')
        print('Enter tip again')
        print()
        tip_percentage = int(input('16, 18 or 20!!!'))

