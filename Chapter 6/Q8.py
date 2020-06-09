#Question 8

def main():
    num = int(input("Enter a positive integer: "))
    isPrime = is_prime(num)

    if isPrime:
        print(num, "is prime!")
    else:
        print(num, "is not prime...")


#Disclaimer: There are MUCH better prime-checking algorithms out there.
def is_prime(num):
    #We test num of primehood
    for divisor in range(2,num):
        if num % divisor == 0:
            return False

    #If num passed all the tests in the for loop then it is prime.
    return True


main()
