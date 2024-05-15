#Keoni Decipulo
#P3LAB
#4/21/24
#calculates to see how much money you have plus change
#uses if and else statements down each cent to see if theres a dollar, quarter, dime, etc.
amount = float(input("Enter the amount of money: $"))


dollars=int(amount)
remaining_cents = round((amount- dollars) * 100)
quarters = remaining_cents // 25
remaining_cents %= 25

dimes = remaining_cents // 10
remaining_cents %= 10

nickels = remaining_cents // 5
remaining_cents %= 5

pennies = remaining_cents

if dollars != 0:
    if dollars == 1:
            print(f"{dollars} dollar")
    else:
            print(f"{dollars} dollars")

if quarters != 0:
    if quarters == 1:
            print(f"{quarters} quarter")
    else:
            print(f"{quarters} quarters")

if dimes != 0:
    if dimes == 1:
            print(f"{dimes} dime")
    else:
            print(f"{dimes} dimes")

if nickels != 0:
    if nickels == 1:
            print(f"{nickels} nickel")
    else:
            print(f"{nickels} nickels")

if pennies != 0:
    if pennies == 1:
            print(f"{pennies} penny")
    else:
            print(f"{pennies} pennies")


    

