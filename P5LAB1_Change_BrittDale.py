def exact_change(user_total=0):
    if user_total <= 0:
        print("no change")
    else:
        dollar = int(user_total/100)
        user_total = user_total % 100 
        quarter = int(user_total/25) 
        user_total = user_total % 25 
        dime = int(user_total/10) 
        user_total = user_total % 10 
        nickel = int(user_total/5) 
        penny = user_total % 5
        if dollar >= 1:
            if dollar == 1:
                print(str(dollar)+" dollar")
            else:
                print(str(dollar)+" dollars")
        if quarter >= 1:
            if quarter == 1:
                print(str(quarter)+" quarter")
            else:
                print(str(quarter)+" quarters")
        if dime >= 1:
            if dime == 1:
                print(str(dime)+" dime")
            else:
                print(str(dime)+" dimes")
        if nickel >= 1:
            if nickel == 1:
                print(str(nickel)+" nickel")
            else:
                print(str(nickel)+" nickels")
        if penny >= 1:
            if penny == 1:
                print(str(penny)+" penny")
            else:
                print(str(penny)+" pennies")
        return dollar, quarter, dime, nickel, penny
                
if __name__ == "__main__":
    user_total = int(input())
    exact_change(user_total)