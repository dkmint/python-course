print("Welcome to the Future Value Calculator\n")

choise = "y"
while choise.lower() == "y":
    monthly_investment = float(input("Enter monthly investment: "))
    interest_rate = float(input("Enter yearly interest rate: "))
    years = int(input("Enter number of years: "))

    monthly_ir = interest_rate / 12 / 100
    months = years * 12

    fv = 0

    for i in range(months):
        fv += monthly_investment
        monthly_interest_amount = fv * monthly_ir
        fv += monthly_interest_amount


    print("Future value:\t\t\t", round(fv, 2))
    choise = input("\nContinue (y/n)?: ")

print("\nBye!")
