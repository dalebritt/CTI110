# A program for calculating meal tip tax
# 09/23/2020
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Dale Britt
#
# Ask user for meal price
food_cost = int(input('Enter Food Cost: '))
print()
# Ask user for tip and tax
tip_percentage = int(input('Enter Tip Percentage: '))
tax_percentage = int(input('Enter Tax Percentage: '))
print()
# Output of users calculated tip and tax percentage
print('Calculated Tip: {:.1f}'.format(tip_percentage))
print('Calculated Tax: {:.1f}'.format(tax_percentage))
print()
# Total meal cost including tip and tax
total_cost = food_cost + tip_percentage + tax_percentage
print('Total cost including tip and tax: {:.1f}'.format(total_cost))


