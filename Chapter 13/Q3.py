#Question 3

def main():
    n = int(input("Enter a positive integer: "))
    lines(n)


def lines(n):
    recLines(1,n)

def recLines(k, n):

    if k <= n:
        for index in range(k):
            print("*", end="")
        print()
        recLines(k+1,n)


main()
