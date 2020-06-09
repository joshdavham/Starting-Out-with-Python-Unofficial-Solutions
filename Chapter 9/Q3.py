#Question 3

def main():
    date = input("Enter the date in the form mm/dd/yyyy: ")
    dateList = date.split("/")
    monthNum = int(dateList[0])
    dayNum = int(dateList[1])
    yearNum = int(dateList[2])

    dateString = getDate(monthNum,dayNum,yearNum)
    print("The date is:", dateString)


def getDate(monthNum, dayNum, yearNum):
    if monthNum == 1:
        month = "January"
    elif monthNum == 2:
        month = "February"
    elif monthNum == 3:
        month = "March"
    elif monthNum == 4:
        month = "April"
    elif monthNum == 5:
        month = "May"
    elif monthNum == 6:
        month = "June"
    elif monthNum == 7:
        month = "July"
    elif monthNum == 8:
        month = "August"
    elif monthNum == 9:
        month = "September"
    elif monthNum == 10:
        month = "October"
    elif monthNum == 11:
        month = "November"
    else:
        month = "December"

    return month + " " + str(dayNum) + ", " + str(yearNum)


main()
