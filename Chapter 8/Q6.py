#Question 6

def main():

    correctanswers = get_correctAnswers()
    studentanswers = get_studentAnswers()
    wrongAnswers = get_wrong_answers(studentanswers, correctanswers)
    numWrong = len(wrongAnswers)
    numRight = len(studentanswers) - numWrong

    if numRight >= 15:
        print("\nThe student passed the exam.")
    else:
        print("\nThe student failed the exam.")

    print(numRight, " questions were answered correctly.", \
          "\n", numWrong, " question were answered incorrectly.", \
          "\nList of question numbers answered incorrectly: ", wrongAnswers, sep = "")

def get_correctAnswers():
    inFile = open("correctanswers.txt", "r")
    correctanswers = [0] * 20
    for index in range(len(correctanswers)):
        correctanswers[index] = inFile.readline().rstrip("\n")

    inFile.close()
    return correctanswers


def get_studentAnswers():
    inFile = open("studentanswers.txt", "r")
    studentAnswers = [0] * 20
    for index in range(len(studentAnswers)):
        studentAnswers[index] = inFile.readline().rstrip("\n")

    inFile.close()
    return studentAnswers

def get_wrong_answers(studentAnswers, correctanswers):
    wrongAnswers = []
    for index in range(len(correctanswers)):
        if studentAnswers[index] != correctanswers[index]:
            wrongAnswers.append(index+1)

    return wrongAnswers


main()
