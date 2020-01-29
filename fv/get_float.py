def get_float():
    while True:
        monthly_investment = float(input("Entry monthly investment: "))
        if monthly_investment <= 0:
            print("Entry must be greater than 0. Please try again.")
            continue
        else:
            return monthly_investment
#            break
