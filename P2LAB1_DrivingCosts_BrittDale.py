total_miles = 20
car_miles_per_gallon = float(input())
gas_dollars_per_gallon = float(input())
gallons_used = total_miles / car_miles_per_gallon
gas_cost_20 = gallons_used * gas_dollars_per_gallon


total_miles = 75
gallons_used = total_miles / car_miles_per_gallon
gas_cost_75 = gallons_used * gas_dollars_per_gallon


total_miles = 500
gallons_used = total_miles / car_miles_per_gallon
gas_cost_500 = gallons_used * gas_dollars_per_gallon
print('{:.2f} {:.2f} {:.2f}'.format(gas_cost_20, gas_cost_75, gas_cost_500))