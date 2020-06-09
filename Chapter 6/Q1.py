#Question 1

def main():
    feet = float(input("Enter the length feet you'd like to convert to inches: "))
    inches = feet_to_inches(feet)
    print("\n", feet, " feet = ", inches, " inches.", sep = "")

def feet_to_inches(feet):
    inches = 12 * feet
    return inches

main()
