#Question 10

def main():
    sentence = input("Please enter a sentence: ")

    char = mostFreqChar(sentence)

    print("\nThe most frequent character is:", char)



def mostFreqChar(sentence):
    #In this function the case of the character is ignored
    mostFreq = sentence[0]
    for index in range(len(sentence)):
        temp = sentence[index]
        mostFreq = compareFreq(mostFreq,temp, sentence)

    return mostFreq

def compareFreq(char1, char2, sentence):
    char1Count = 0
    char2Count = 0

    for index in range(len(sentence)):
        currChar = sentence[index]
        if currChar == char1:
            char1Count += 1
        elif currChar == char2:
            char2Count += 1

    if char1Count > char2Count:
        return char1
    else:
        return char2




main()
