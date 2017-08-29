'''
### Problem 0003 ### Largest prime factor ###
What is the largest prime factor of the number 600851475143 ?
'''
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % 2 == 0:
                return False
        return True
    return False

def get_primes():
    number = 3
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_0003(number):
    largestPrimeFactor = 2
    index = 0
    for primeNumber in get_primes():  
        index += 1
        if index % 1000000 == 0:
            print(primeNumber)
        if primeNumber <= number:
            if number % primeNumber == 0:
                largestPrimeFactor = primeNumber
                print(largestPrimeFactor)
        else:
            print('Largest prime factor of the number {} is {}.'.format(number, largestPrimeFactor))
            return

solve_0003(60086)