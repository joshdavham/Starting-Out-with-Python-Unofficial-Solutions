#Question 6

def main():
    n = int(input("Enter a positive integer: "))

    mySum = getSum(n)

    print("\nThe sum from 1 to n is", mySum)


def getSum(n):

    if n == 1:
        return 1
    else:
        return n + getSum(n-1)



main()
