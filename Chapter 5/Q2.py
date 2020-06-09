#Question 2

#Global constant
CAL_PER_MIN = 3.9

def main():

    for time in range(10,31,5):
        caloriesBurned = time * CAL_PER_MIN

        print("After", time, "minutes you've burned", caloriesBurned, "calories.")

        print()#Eats a line

main()
