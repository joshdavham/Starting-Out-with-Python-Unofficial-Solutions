import random
#Question 2

def main():

    lotteryNumber = [0] * 7
    for index in range(len(lotteryNumber)):
        lotteryNumber[index] = random.randint(0,9)

    #Display the result
    print("\nThe lottery number:", \
          "\n", lotteryNumber, sep = "")


main()
