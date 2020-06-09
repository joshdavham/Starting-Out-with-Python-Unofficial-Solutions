#Question 10

numShares = 1000
pricePerShare = 32.87 #In dollars
percentCommision = 0.02 #2% in commision

priceStock = pricePerShare * numShares
amountCommision = priceStock * percentCommision
moneyJoe = 0 - priceStock - amountCommision #The amount of money Joe made after the stock purchase

print("Joe paid $", format(priceStock, '.2f'), " for the stock.", \
      "\nJoe paid his stockbroker $", format(amountCommision, '.2f'), " in commision after buying the stock.", sep = "")

numSold = 1000 #The amount of shares Joe sold
pricePerShare = 33.92 #The pricePerShare 2 weeks later
priceSold = numSold * pricePerShare #The amount of money he recieved for the sell
amountCommision = priceSold * percentCommision #percentCommision did not change but amountCommision did.
moneyJoe = moneyJoe + priceSold - amountCommision #The amount Joe made after selling his shares

print("\nJoe sold his stock for $", format(priceSold, '.2f'), \
      "\nJoe paid his stockbroker $", format(amountCommision, '.2f'), " in commision after selling his stock." \
      "\nJoe is now left with $", format(moneyJoe, '.2f'), sep = "")
