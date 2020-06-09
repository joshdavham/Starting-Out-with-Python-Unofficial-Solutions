#Question 2

import random

def main():
    #Random integers between 1 and 1000
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)

    #The true answer...
    ans = num1 + num2

    #The user's answer:
    userAns = int(input(str(num1) + " + " + str(num2) + " = "))

    if ans == userAns:
        print("\nYour answer is correct!")
    else:
        print("\nYour answer is incorrect...")

main()
