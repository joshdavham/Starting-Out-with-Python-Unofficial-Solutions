#Question 9

def main():

    print("List of primes between 1 and 100:", \
          "----------------------------------\n")
    for num in range(1,101):
        if is_prime(num):
            print(num)


#Disclaimer: There are MUCH better prime-checking algorithms out there.
def is_prime(num):
    #We test num of primehood
    for divisor in range(2,num):
        if num % divisor == 0:
            return False

    #If num passed all the tests in the for loop then it is prime.
    return True


main()
