#Question 6

def main():

    set1 = fileToSet("Q6input1.txt")
    set2 = fileToSet("Q6input2.txt")

    unionSet = set1 | set2
    print("\nWords contained in either file:", \
          "\n", unionSet, sep="")

    interSet = set1 & set2
    print("\nWords contained in both files:", \
          "\n", interSet, sep="")

    diffSet1 = set1 - set2
    print("\nWords contained in file1 but not file2:", \
          "\n", diffSet1, sep="")

    diffSet2 = set2 - set1
    print("\nWords contained in file2 but not file1:", \
          "\n", diffSet2, sep="")

    symmSet = set1 ^ set2
    print("\nWords contained in either set but not in both:", \
          "\n", symmSet, sep="")




def fileToSet(txtFile):
    wordSet = set()

    inFile = open(txtFile, "r")

    line = inFile.readline()

    while line != "":
        wordSet.update(line.split())
        line = inFile.readline()

    inFile.close()

    return wordSet




main()
