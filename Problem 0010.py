from math import sqrt

'''
### Problem 0010 ### Summation of primes ###
Find the sum of all the primes below two million.
'''

def is_prime(number):
    '''Check if prime number'''
    if number > 1:
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        for i in range(3, int(sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True
    return False

def get_primes(number):
    '''Generate infinite series of prime numbers.'''
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_0010(limit):

    total = 2
    index = 0
    for next_prime in get_primes(3):
        if next_prime < limit:
            total += next_prime             
            index += 1
        else:
            print(total)
            return

solve_0010(limit=2e6)