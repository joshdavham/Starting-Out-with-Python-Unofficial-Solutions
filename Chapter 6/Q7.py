import random
#Question 7

def main():
    numEven = 0
    for x in range(0,100):
        
        randNum = random.randint(1,1000) #Random number between 1 & 1000

        if randNum % 2 == 0:
            numEven += 1

    numOdd = 100 - numEven
    print("Of the 100 random numbers generated", numOdd, "were odd and", numEven, "were even.")

main()
