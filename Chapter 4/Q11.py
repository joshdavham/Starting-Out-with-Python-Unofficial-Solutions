#Question 11

def main():
    seconds = float(input("Enter the number of seconds: "))

    minutes = seconds / 60

    hours = seconds / 3600

    days = seconds / 86400

    print("\nIn", seconds, "seconds there are...")
    print(minutes, "minutes.")
    print(hours, "hours.")
    print(days, "days.")


main()
