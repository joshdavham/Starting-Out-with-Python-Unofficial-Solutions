import random
#Question 5

def main():

    #Initialize a random list 10 entries long
    myList = [0] * 10
    for index in range(len(myList)):
        myList[index] = random.randint(1,100)

    print("List contents: " + str(myList))

    total = getTotal(myList)


    print("\nTotal: " + str(total))


def getTotal(myList):

    return recGetTotal(myList,0)

def recGetTotal(myList, index):

    if index == len(myList) - 1:
        return myList[index]
    else:
        return myList[index] + recGetTotal(myList,index+1)

main()
