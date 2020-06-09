import random
#Question 11

def main():
    keepPlaying = True
    while keepPlaying:

        ans = random.randint(1,100)

        num = int(input("Im thinking of a number between 1 and 100, guess? "))
        while num != ans:
            if num < ans:
                num = int(input("Too low, try again. "))
            elif num > ans:
                num = int(input("Too high, try again. "))

        print("\nContratulations", num, "is correct!.\n" \
              "--------------------------------")

        userAns = str(input("Keep playing? Enter y if yes: "))
        if userAns == "y" or userAns == "Y":
            keepPlaying = True
        else:
            keepPlaying = False

        print("")#Eats a line



main()
