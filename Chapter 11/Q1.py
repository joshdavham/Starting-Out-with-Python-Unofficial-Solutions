#Question 1

class Pet:

    #Instance variables initialized to neutral values
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():

    myPet = Pet()
    name = input("Enter the name of your pet: ")
    myPet.set_name(name)

    animal_type = input("Enter your pet's type: ")
    myPet.set_animal_type(animal_type)

    age = input("Enter the age of your pet: ")
    myPet.set_age(age)

    print("\nYour Pet:", \
          "\n---------", \
          "\nName:", myPet.get_name(), \
          "\nType:", myPet.get_type(), \
          "\nAge:", myPet.get_age())




main()
