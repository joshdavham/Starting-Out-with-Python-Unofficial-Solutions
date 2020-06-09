import pickle
#Question 8

def main():

    inFile = open("emails.dat", "rb")
    emails = pickle.load(inFile)
    inFile.close()

    keepGoing = True
    while keepGoing:
        print("\nEnter 1 to lookup email address,", \
              "\nEnter 2 to add a new email,", \
              "\nEnter 3 to change an existing email address,", \
              "\nEnter 4 to delete an existing email address,", \
              "\nEnter anything else to exit the program.")

        userInput = input("\nWhat would you like to do? ")

        if userInput == "1":
            name = input("\nEnter the name of the person who's email you'd like to find: ")
            if name in emails:
                email = emails[name]
                print("Name:", name, "Email:", email)
            else:
                print("That user does not exist.")


        elif userInput == "2":
            name = input("\nEnter the name of the person who's email you'd like to add: ")
            email = input("Enter " + name + "'s email: ")
            emails[name] = email


        elif userInput == "3":
            name = input("\nEnter the name of the person whos email you'd like to change: ")
            if name in emails:
                email = input("Enter " + name + "'s new email address: ")
                emails[name] = email
            else:
                print("That user does not exist.")


        elif userInput == "4":
            name = input("\nEnter the name of the perons you'd like to delete from the email database: ")
            if name in emails:
                del emails[name]
            else:
                print("That user does not exist.")

        else:
            keepGoing = False


    #The email dictionary is pickled and saved
    outFile = open("emails.dat", "wb")
    pickle.dump(emails, outFile)
    outFile.close()


main()
