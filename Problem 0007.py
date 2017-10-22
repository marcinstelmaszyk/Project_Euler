'''
### Problem 0007 ### 10001st prime ###
What is the 10 001st prime number?
'''
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True
    return False

def get_primes():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_0007(prime_number):
    primes = get_primes()
    for i in range(1, prime_number+1):
        lastPrimeFound = next(primes)
        print('{} prime number is {}.'.format(i, lastPrimeFound))

solve_0007(10001)