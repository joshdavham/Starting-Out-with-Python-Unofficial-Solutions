#Question 2

def main():
    numbers = input("Enter a string of digits with no spacing between them: ")
    total = 0
    for index in range(len(numbers)):
        total += int(numbers[index])

    print("The total is:", total)


main()
