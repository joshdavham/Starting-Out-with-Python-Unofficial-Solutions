#Question 7

def main():
    days = int(input("How many days do you plan to work? "))

    print("Day #\tSalary", \
          "\n--------------")

    salary = 0.005
    totalPay = 0
    for day in range(1, days+1):
        salary = 2 * salary
        totalPay += salary
        print(day, "\t$", format(salary, '.2f'), sep = "")

    print("\nTotal Pay: $", format(totalPay, '.2f'), sep = "")

main()
