#Question 8

percentTip = 0.15 #15% tip
percentTax = 0.07 #7% tax

mealCost = float(input("How much did your meal cost? "))

tipCost = percentTip * mealCost
taxCost = percentTax * mealCost
total = mealCost + tipCost + taxCost

print("Meal Price: $", format(mealCost, '.2f'), \
      "\nTip: $", format(tipCost, '.2f'), \
      "\nTax: $", format(taxCost, '.2f'),
      "\nTotal: $", format(total, '.2f'), sep = "")
