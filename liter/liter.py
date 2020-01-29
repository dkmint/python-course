print("The Miles Per Kilometer Program\n")

kms_driven = float(input("Enter kilometers driven:\t\t"))
liters_used = float(input("Enter liters of gas used:\t"))

kpl = round(kms_driven / liters_used, 2)
print("\nKilometers per Liter:\t\t", kpl)
print("\nBye")
