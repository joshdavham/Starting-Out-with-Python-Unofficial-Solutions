#Question 6

stateTax = 0.04 #4% tax
countyTax = 0.02 #2% tax

amountPurchase = float(input("How much is your purchase? "))

amountStateTax = stateTax * amountPurchase #How much must be paid to the stateTax
amountCountyTax = countyTax * amountPurchase #How much must be paid to the countyTax
totalTax = amountCountyTax + amountStateTax

total = amountPurchase + totalTax #How much the customer must pay

print("Amount purchased: $", format(amountPurchase, '.2f'), \
      "\nState-Tax: $", format(amountStateTax, '.2f'), \
      "\nCounty-Tax: $", format(amountCountyTax, '.2f'), \
      "\nTotal Tax: $", format(totalTax, '.2f'), \
      "\nTotal: $", format(total, '.2f'), sep = "")
