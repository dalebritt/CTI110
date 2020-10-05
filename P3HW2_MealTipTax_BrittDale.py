# A program for calculating meal tip tax
# 10/04/2020
# CTI-110 P3HW2 - Meal Tip Tax Calculator
# Dale Britt
#
# Set tax
tax_percentage = 6.0
# Ask user for meal price
food_cost = int(input('Enter Food Cost: '))
# Ask user for tip
tip_percentage = int(input('Enter Tip Percentage of 15, 18, or 20: '))
print()
if tip_percentage in (15, 18, 20):
    # Output of users calculated tip and tax percentage
    print('Calculated Tip: {:.1f}'.format(tip_percentage))
    print('Calculated Tax: {:.1f}'.format(tax_percentage))
    # Total meal cost including tip and tax
    total_cost = food_cost + tip_percentage + tax_percentage
    print('Total cost including tip and tax: {:.1f}'.format(total_cost))
else:
    # Error if tip amount out of requested input
    print('Invalid, please enter 15, 18, or 20 for tip percentage')
