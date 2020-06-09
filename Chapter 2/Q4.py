#Question 4

salesTax = 0.06 #6% tax

price1 = float(input("How much does the first item cost? "))
price2 = float(input("How much does the second item cost? "))
price3 = float(input("How much does the third item cost? "))
price4 = float(input("How much does the fourth item cost? "))
price5 = float(input("How much does the fifth item cost? "))

#Subtotal - total price before tax
subTotal = price1 + price2 + price3 + price4 + price5
total = subTotal * (1 + salesTax)
amountTax = total - subTotal

print("\nYour subtotal: $", format(subTotal, '.2f'), \
      "\nTax Paid: $", format(amountTax, '.2f'), \
      "\nYour Total: $", format(total, '.2f'), sep = "")
