import random
#Question 4

def main():

    #Initialize a random list 10 entries long
    myList = [0] * 10
    for index in range(len(myList)):
        myList[index] = random.randint(1,100)

    print("List contents: " + str(myList))

    largestEntry = largest(myList)

    print("\nThe largest entry of the list: " + str(largestEntry))


def largest(myList):
    return recLargest(myList, 0, myList[0])

def recLargest(myList, index, largestEntry):

    currEntry = myList[index]
    if currEntry > largestEntry:
        largestEntry = currEntry

    #Base case - We've made it to the end of the list
    if index == len(myList) - 1:
        return largestEntry

    else:
        return recLargest(myList,index+1,largestEntry)


main()
