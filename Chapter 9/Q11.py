#Question 11

def main():
    sentence = input("Enter a sentence with no spaces but with each word capitalized: ")


    sentence = processSentence(sentence)

    print("\n", sentence, sep = "")

def processSentence(sentence):
    result = ""
    for index in range(len(sentence)):
        currChar = sentence[index]
        if currChar == currChar.upper():
            result += " "
        result += currChar

    return result.strip()



main()
