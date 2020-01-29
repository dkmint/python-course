print("Welcome to the Future Value Calculator\n")

choise = "y"
while choise.lower() == "y":
#    monthly_investment = float(input("Enter monthly investment: "))
    while True:
        monthly_investment = float(input("Entry monthly investment: "))
        if monthly_investment <= 0:
            print("Entry must be greater than 0. Please try again.")
            continue
        else:
            break
    while True:
        interest_rate = float(input("Enter yearly interest rate: "))
        if interest_rate <= 0 or interest_rate > 15 :
            print("Entry must be greater than 0 and less than or equal to 15.")
            print("Please try again")
            continue
        else:
            break
    while True:
        years = int(input("Enter number of years: "))
        if years <= 0 or years > 50:
            print("Entry must be greater than 0 and less than or equal to 50.")
            print("Please try again")
            continue
        else:
            break

    monthly_ir = interest_rate / 12 / 100
    months = years * 12

    fv = 0
    ycount = 0
    mcount = 0
    for i in range(months):
        mcount += 1
        fv += monthly_investment
        monthly_interest_amount = fv * monthly_ir
        fv += monthly_interest_amount
        if (mcount % 12) == 0:
            fv = round(fv, 2)
            ycount += 1
            print(f'Year = {ycount} Future Value = {fv}')

    choise = input("\nContinue (y/n)?: ")

print("\nBye!")
