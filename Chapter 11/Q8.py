import random
#Question 8

class Question:

    def __init__(self, question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
        self.__question = question
        self.__answer = answer
        self.__answers = {}

        #This next part assigns the possible answers
        #To random keys in the answer dictionary
        answerSet = [1,2,3,4]

        randomIndex = random.choice(answerSet)
        self.__answers[randomIndex] = answer
        answerSet.remove(randomIndex)

        randomIndex = random.choice(answerSet)
        self.__answers[randomIndex] = wrongAnswer1
        answerSet.remove(randomIndex)

        randomIndex = random.choice(answerSet)
        self.__answers[randomIndex] = wrongAnswer2
        answerSet.remove(randomIndex)

        randomIndex= random.choice(answerSet)
        self.__answers[randomIndex] = wrongAnswer3
        answerSet.remove(randomIndex)



    def getQuestion(self):
        return self.__question

    def getAnswer(self):
        return self.__answer

    def testAnswer(self,userAnswer):

        if self.__answers[int(userAnswer)] == self.__answer:
            return True
        else:
            return False

    def displayAnswers(self):

        for index in range(len(self.__answers)):
            print(str(index+1) + ": " + str(self.__answers[index+1]) + " \n")


def main():

    questions = generateQuestions()

    player1Score = 0
    player2Score = 0

    for index in range(1,11,2):
        question = questions[index]
        print("\nPlayer 1: \n--------\n" + question.getQuestion() + "\n---------------------------------")
        question.displayAnswers()

        userAnswer = input(": ")
        if question.testAnswer(userAnswer):
            print("\nCORRECT!")
            player1Score += 1
        else:
            print("\nfalse... It was " + question.getAnswer())

        question = questions[index+1]
        print("\nPlayer 2: \n--------\n" + question.getQuestion() + "\n---------------------------------")
        question.displayAnswers()

        userAnswer = input(": ")
        if question.testAnswer(userAnswer):
            print("\nCORRECT!")
            player2Score += 1
        else:
            print("\nfalse... It was " + question.getAnswer())





    print("\n\nPlayer 1 final score: " + str(player1Score) +
          "\nPlayer 2 final score: " + str(player2Score))

    if player1Score > player2Score:
         print("\nPlayer 1 wins!", \
               "\n--------------")
    elif player1Score < player2Score:
         print("\nPlayer 2 wins!", \
               "\n--------------")
    else:
         print("\nTIE!", \
               "\n--------------")

#Returns a dictionary of questions
def generateQuestions():
    questions = {}

    questions[1] = Question("What is the capital of Canada?","Ottawa","Toronto","Vancouver","Quebec City")

    questions[2] = Question("Who is the Prime Minister of Canada?","Justin Trudeau","Stephen Harper","Theresa May","Angela Merkel")

    questions[3] = Question("When was the confederation of Canada?","1867","1776","1835","1710")

    questions[4] = Question("What is the population of Canada?","35 million","30 million","40 million","45 million")

    questions[5] = Question("What is Canada's national sport","Hockey and Lacrosse","Hockey","Lacrosse","Neither")

    questions[6] = Question("Who discovered Canada?","Jacques Cartier","Samuel Champlain","Columbus","Adam Smith")

    questions[7] = Question("Who was the first Prime Minister of Canada?","John A. Macdonald","Pierre Trudeau","Kim Campbell","Lester B. Pearsons")

    questions[8] = Question("When is Canada Day?","July 1","July 4","June 1","June 4")

    questions[9] = Question("What year did Nunavut become a territory?","1999","1983","2001","1953")

    questions[10] = Question("How many Provinces does Canada hold?","10","13","11","12")

    return questions

main()
