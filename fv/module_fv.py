def display_title():
    print("Welcome to the Future Value Calculator")
    print()


def get_float(*args):
    while True:
        for argument in args:
            print(argument, end="")
        print()
#        value = float(input("Enter Number: "))
        value = float(input())
        if value <= 0 or value > 1000:
            print("Entry must be greater than 0 and less than or equal to 1000.")
            print("Please try again.")
            continue
        else:
            break
    return value

def get_int(*args):
    while True:
#        value = int(input("Enter Integer Number: "))
        for argument in args:
            print(argument, end="")
        print()
        value = int(input())
        if value <= 0 or value > 50:
            print("Entry must be greater than 0 and less than or equal to 50.")
            print("Please try again.")
            continue
        else:
            break
    return value


def get_fv(monthly_investment, interest_rate, years):
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

