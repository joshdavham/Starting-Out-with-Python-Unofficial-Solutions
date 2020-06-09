#Question 1

def main():
    n = int(input("Enter a positive integer to count to: "))
    seq = printSequence(n)
    print("\n" + seq)



def printSequence(n):
    if n > 1:
        return printSequence(n-1) + str(n)
    elif n == 1:
        return str(1)

main()
