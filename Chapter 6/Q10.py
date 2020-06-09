#Question 10

def main():
    p = float(input("Enter your account's present value: "))
    i = float(input("Enter your monthly interest rate (in decimals): "))
    t = float(input("Enter the amount of months you will save: "))

    f = future_value(p,i,t)
    print("The future of your account is $", format(f,'.2f'), ".", sep = "")

def future_value(p, i, t):
    f = p * ((1 + i)**t)
    return f

main()
