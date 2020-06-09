#Question 2

class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed







def main():

    myCar = Car("2005","Lamborghini")

    print("\nThe Car is accelerating:", \
          "\n------------------------")
    for index in range(5):
        myCar.accelerate()
        currSpeed = myCar.get_speed()
        print("The car is currently travelling at a speed of:", currSpeed)

    print("\nThe Car is braking:", \
          "\n-------------------")
    for index in range(5):
        myCar.brake()
        currSpeed = myCar.get_speed()
        print("The car is currently travelling at a speed of:", currSpeed)


main()
