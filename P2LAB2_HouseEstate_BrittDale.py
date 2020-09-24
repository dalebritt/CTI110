current_price = int(input())
last_months_price = int(input())
change_in_price = current_price - last_months_price
print("This house is ${}. The change is ${} since last month.".format(current_price, change_in_price))
estimated_mortgage_year = current_price * 0.051
estimated_mortgage_month = estimated_mortgage_year / 12
print('The estimated monthly mortgage is ${:.2f}.'.format(estimated_mortgage_month))
