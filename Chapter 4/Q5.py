#Question 5

def main():
    color1 = input("Welcome to the Colour Mixer, please enter " +
                   "either 'Red', 'Blue', or 'Yellow' for the first colour: ")

    color2 = input("\nPlease enter either 'Red', 'Blue', or 'Yellow' for the second colour: ")

    #If at least one of colours entered are not primary.
    if ((color1 != "Red") and (color1 != "Blue") and (color1 != "Yellow")) \
    or ((color2 != "Red") and (color2 != "Blue") and (color2 != "Yellow")):

        print("\nERROR: You may only enter primarily colors.")

    else:
        mixColours(color1, color2)

def mixColours(color1, color2):

    if(color1 == color2):
        result = color1
        print("\n", color1, " + ", color2, " = ", result, sep = "")

    elif (color1 == "Red" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Red"):
        result = "Orange"
        print("\n", color1, " + ", color2, " = ", result, sep = "")

    elif (color1 == "Red" and color2 == "Blue") or (color1 == "Blue" and color2 == "Red"):
        result = "Purple"
        print("\n", color1, " + ", color2, " = ", result, sep = "")

    else:#The only possibility left is one color being yellow and the other being Blue
        result = "Green"
        print("\n", color1, " + ", color2, " = ", result, sep = "")

main()
