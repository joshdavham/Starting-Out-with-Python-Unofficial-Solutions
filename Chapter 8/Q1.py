#Question 1

def main():

    sales = get_input()
    total = get_total(sales)
    print("\nTotal weekly sales: $", total, sep = "")

def get_input():
    sales = [0] * 7
    for day in range(7):
        sales[day] = float((input("What were the sales for day " + str(day+1) + "? ")))

    return sales


def get_total(sales):
    total = 0
    for day in range(len(sales)):
        total += sales[day]

    return total



main()
