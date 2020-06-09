import random
#Qustion 2

def main():
    statesAndCapitals = {"Alabama":"Montgomery", \
                     "Alaska":"Juneau", \
                     "Arizona":"Phoenix", \
                     "Arkansas":"Little Rock", \
                     "California":"Sacramento", \
                     "Colorado":"Denver", \
                     "Conneticut":"Hartford", \
                     "Delaware":"Dover", \
                     "Florida":"Tallahasee", \
                     "Georgia":"Atlanta", \
                     "Hawaii":"Honolulu", \
                     "Idaho":"Boise", \
                     "Illinois":"Springfield", \
                     "Indiana":"Indianapolis", \
                     "Iowa":"Des Moines", \
                     "Kansas":"Topeka", \
                     "Kentucky":"Frankfort", \
                     "Louisiana":"Baton Rouge", \
                     "Maine":"Augusta", \
                     "Maryland":"Annapolis", \
                     "Massachusetts":"Boston", \
                     "Michigan":"Lansing", \
                     "Minnesota":"St. Paul", \
                     "Mississippi":"Jackson", \
                     "Missouri":"Jefferson City", \
                     "Montana":"Helena", \
                     "Nebraska":"Lincoln", \
                     "Nevada":"Carson City", \
                     "New Hampshire":"Concord", \
                     "New Jersey":"Trenton", \
                     "New Mexico":"Santa Fe", \
                     "New York":"Albany", \
                     "North Carolina":"Raleigh", \
                     "North Dakota":"Bismark", \
                     "Ohio":"Columbus", \
                     "Oklahoma":"Oklahoma City", \
                     "Oregon":"Salem", \
                     "Pennsylvania":"Harrisburg", \
                     "Rhode Island":"Providence", \
                     "South Carolina":"Columbia", \
                     "South Dakota":"Pierre", \
                     "Tennessee":"Nashville", \
                     "Texas":"Austin", \
                     "Utah":"Salt Lake City", \
                     "Vermont":"Montpelier", \
                     "Virginia":"Richmond", \
                     "Washington":"Olympia", \
                     "West Virginia":"Charleston", \
                     "Wisconsin":"Madison", \
                     "Wyoming":"Cheyenne"}
    states = list(statesAndCapitals.keys())


    numQuestions = int(input("How many states would you like to be quizzed on? "))

    for count in range(numQuestions):

        randIndex = random.randint(0,len(states)-1)
        state = states[randIndex]
        capital = statesAndCapitals[state]

        city = input("\nWhat is the capital of " + state + "? ")

        if city == capital:
            print("Correct!")
        else:
            print("Wrong... It was " + capital)



main()
