#Question 12

def main():
    engSentence = input("Enter a sentence: ")

    pigSentence = pigLatin(engSentence)

    print("\nEnglish:", engSentence, \
          "\n\nPig Latin:", pigSentence)


def pigLatin(engSentence):
    result = ""
    engWords = engSentence.split()

    for index in range(len(engWords)):
        currWord = engWords[index]

        if len(currWord) == 1:
            result += currWord + "ay "
        else:
            firstChar = currWord[0]
            result += currWord[1:] + firstChar + "ay "

    return result


main()
