#Question 2

def main():

    x = int(input("Enter a positive integer: "))
    y = int(input("Enter another positive integer: "))

    z = multiply(x,y)

    print("\nThe product is:", z)

#Assumes that x and y are positive integers.
def multiply(x, y):

    if y == 1:
        return x
    else:
        return x + multiply(x,y-1)

main()
