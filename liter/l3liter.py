print("The Miles Per Kilometer Program\n")

choise = "y"

while choise.lower() == "y":
    kms_driven = float(input("Enter kilometers driven:\t"))
    liters_used = float(input("Enter liters of gas used:\t"))
    cost = float(input("Enter cost per liter:\t\t"))

    gas_cost = round(liters_used * cost, 2)
    kpl = round(kms_driven / liters_used, 2)
    cpk = round(gas_cost / kms_driven, 2)
    print("\nKilometers per Liter:\t", kpl)
    print("Total gaz cost:\t\t", gas_cost)
    print("Cost per kilometer:\t", cpk)

    choise = input("\nGet entries for another trip (y/n)?: ")

print("\nBye")
