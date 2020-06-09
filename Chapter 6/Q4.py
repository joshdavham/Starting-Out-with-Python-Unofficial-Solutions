#Question 4

#Global constant
GRAVITY = 9.8

def main():
    for time in range(0,11):
        distance = falling_distance(time)
        print("After", time, "seconds, the object has fallen", format(distance, '.2f'), "meters.")

def falling_distance(time):
    distance = (1 / 2) * GRAVITY * (time**2)
    return distance

main()
