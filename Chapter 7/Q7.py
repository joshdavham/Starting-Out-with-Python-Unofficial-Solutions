import random
#Question 7

def main():
    value = int(input("How many random numbers would you like to write to the file? "))

    outFile = open("numbers.txt", "w")
    for x in range(value):
        num = random.randint(1,100)
        outFile.write(str(num) + "\n")

    outFile.close()




main()
