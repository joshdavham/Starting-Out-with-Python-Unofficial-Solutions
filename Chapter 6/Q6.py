#Question 6

def main():
    test1 = float(input("Enter the first test score: "))
    letterGrade = determine_grade(test1)
    print("Test 1 scored a(n) ", letterGrade, ".", sep = "")

    test2 = float(input("\nEnter the second test score: "))
    letterGrade = determine_grade(test2)
    print("Test 2 scored a(n) ", letterGrade, ".", sep = "")

    test3 = float(input("\nEnter the third test score: "))
    letterGrade = determine_grade(test3)
    print("Test 3 scored a(n) ", letterGrade, ".", sep = "")

    test4 = float(input("\nEnter the fourth test score: "))
    letterGrade = determine_grade(test4)
    print("Test 4 scored a(n) ", letterGrade, ".", sep = "")

    test5 = float(input("\nEnter the fifth test score: "))
    letterGrade = determine_grade(test5)
    print("Test 5 scored a(n) ", letterGrade, ".", sep = "")

    avg = calc_average(test1,test2,test3,test4,test5)

    print("\nThe test average:", format(avg, '.2f'))

def calc_average(test1, test2, test3, test4, test5):
    avg = (test1 + test2 + test3 + test4 + test5) / 5
    return avg

def determine_grade(test):
    if test <= 100 and test >= 90:
        letterGrade = "A"
    elif test <= 89 and test >= 80:
        letterGrade = "B"
    elif test <= 79 and test >= 70:
        letterGrade = "C"
    elif test <= 69 and test >= 60:
        letterGrade = "D"
    elif test < 60:
        letterGrade = "F"

    return letterGrade

main()
