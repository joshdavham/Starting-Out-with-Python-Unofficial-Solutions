#Question 8

def main():

    m = int(input("\nEnter a non-negative integer for m: "))
    n = int(input("Enter a non-negative integer for n: "))

    outPut = ack(m,n)

    print("\nAckermann(" + str(m) + "," + str(n) + ") = " + str(outPut))


def ack(m,n):

    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))

main()
