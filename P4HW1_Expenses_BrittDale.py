# CTI-110
# P4HW1 - Expenses
# Dale Britt
# 10/16/2020
# Program for calculating users expenses
# Takes starting amount and expenses as user input and subtracts expenses to give current balance

starting_amount = int(input('Enter starting amount in account $'))
current_balance = starting_amount
print()

user_input = 'y'

i = 1
while user_input != 'n':
    user_expense = int(input('Enter expense {}: '.format(i)))
    user_input = input('Do you want to enter another expense?(y/n) ')
    if user_input in ('y', 'n'):
        i = i + 1
        current_balance = current_balance - user_expense
    else:
        print('Invalid input. Please enter y or n')
    print()

i = i - 1

print('Amount in account before expenses subtracted ${:.2f}'.format(starting_amount))
print('Number of expenses entered: {}'.format(i))
print('Amount in account after expenses subtracted is ${:.2f}'.format(current_balance))    


