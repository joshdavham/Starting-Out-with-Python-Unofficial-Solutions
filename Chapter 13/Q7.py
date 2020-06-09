#Question 7

def main():
    a = float(input("Enter a number: "))
    n = int(input("Enter a positive integer: "))

    b = power(a,n)

    print("\n" + str(a) + "^" + str(n) + " = " + str(b))

def power(a,n):
    if n == 1:
        return a
    else:
        return a * power(a,n-1)

main()
