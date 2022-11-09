from math import sqrt


def sieve_Eratosthenes(x):
    primes = []
    count = 1
    primes = [True] * (x + 1)  
    for i in range(2, int(sqrt(x + 1))):
        if primes[i]:
            for j in range(i + i, x + 1, i):
                primes[j] = False

    for i in range(2, x + 1):
        if primes[i]:
            print(f"Number {count} : {i}")
            count += 1

    return print(f"The number of primes in a given range is: {count}")


x = int(input("Enter a positive number greater than 2:"))
while x <= 2:
    x = int(input("Enter positiv number:"))
    
sieve_Eratosthenes(x)
