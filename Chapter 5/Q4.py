#Question 4

def main():
    speed = int(input("What is the speed of the veihicle in mp? "))
    time = int(input("How many hours has it traveled? "))

    print("Hour\tDistance Traveled", \
          "\n----------------------------")

    for hour in range(1, time+1):
            distance = hour * speed
            print(hour, "\t", distance)


main()
