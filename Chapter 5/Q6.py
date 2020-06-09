#Question 6

def main():
    print("Celsius\tFarenheit", \
          "\n-----------------")
    for celsius in range(21):
        farenheit = ((9 / 5) * celsius) + 32
        print(celsius, "\t", format(farenheit, '.2f'))

main()
