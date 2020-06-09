#Question 2

def main():
    length1 = float(input("Enter the length of rectangle1: "))
    width1 = float(input("Enter the width of rectangle2: "))

    length2 = float(input("Enter the length of rectangle2: "))
    width2 = float(input("Enter the width of rectangle2: "))

    #The area of rectangle1
    area1 = length1 * width1

    #The area of rectangle2
    area2 = length2 * width2

    #We now compare the two areas
    compAreas(area1, area2)

def compAreas(area1, area2):
    if area1 > area2:
        print("\nThe area of rectangle1 is greater than the area of rectangle2.")

    elif area1 < area2:
        print("\nThe area of rectangle2 is greater than the area of rectangle1.")

    else:#area1 == area2
        print("\nThe area of rectangle1 is equal to the area of rectangle2.")



main()
