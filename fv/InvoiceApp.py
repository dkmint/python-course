print("Welcome to the Invoice Total Calculator")
print()
subtotal = float(input("Enter subtotal: \n"))
discountPercent = .2
discountAmount = subtotal * discountPercent
invoiceTotal = subtotal - discountAmount

print("Discount Percent: %5.2f\nDiscount Amount: %6.2f\nInvoice Total: %8.2f" % 
     (discountPercent, discountAmount, invoiceTotal))
