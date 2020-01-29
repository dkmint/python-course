from module_fv import display_title, get_float, get_int, get_fv

again = 'y'
display_title()

while again.lower() == 'y':
    monthly_investment = get_float("Enter Monthly Investment:  0, 1000")
    interest_rate = get_float("Enter Interest Rate:  0, 15")
    years = get_int("Enter Number of Years:  0, 50")
    get_fv(monthly_investment, interest_rate, years)
    
    again = input("\nContinue (y/n)?: ")

print("\nBye!")    


