#Question 1

def main():
    rooms = {"CS101":3004, "CS102":4501, "CS103":6755, "NT110":1244, "CM241":1411}
    teachers = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}
    times = {"CS101":"8:00 a.m.", "CS102":"9:00 a.m.", "CS103":"10:00 a.m.", "NT110":"11:00 a.m.", "CM241":"1:00 a.m."}

    key = input("Enter a course key: ")

    print("\nRoom number: " + str(rooms[key]) + \
          "\nTeacher: " + teachers[key] + \
          "\nTime: " + times[key])



main()
