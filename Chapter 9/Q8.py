#Question 8

def main():
    sentence = input("Enter a sentence to be capitalized: ")

    sentence = capitalizer(sentence)

    print("\n", sentence, sep = "")


def capitalizer(sentence):
    words = sentence.split()

    result = ""
    for index in range(len(words)):
        word = words[index]
        word1 = word[0:1].upper()
        word2 = word[1:]
        word = word1 + word2

        result += word + " "

    return result.strip()



main()
