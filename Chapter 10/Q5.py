#Question 5

def main():

    wordFreq = dict()

    inFile = open("Q5input.txt", "r")

    line = inFile.readline()

    while line != "":
        words = line.split()

        for index in range(len(words)):
            word = words[index]
            if word in wordFreq:
                wordFreq[word] += 1
            else:
                wordFreq[word] = 1

        line = inFile.readline()

    inFile.close()

    print("\nWord Frequences:", \
          "\n----------------", sep="")
    for index in range(len(wordFreq)):
        pair = wordFreq.popitem()
        word = pair[0]
        freq = pair[1]


        print(word + " occured " + str(freq) + " time(s).")



main()
