#Question 3

def main():
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))

    result = maximum(int1, int2)
    print("\nThe biggest integer is:", result)

def maximum(int1, int2):
    if int1 > int2:
        result = int1
    else:
        result = int2
    return result
main()
