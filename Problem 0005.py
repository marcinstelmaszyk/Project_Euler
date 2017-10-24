'''
### Problem 0005 ### Smallest multiple ###
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def factorToPrimes(number):
    factorsFound = [number]
    for i in range(2, number):
        while True:
            if number%i == 0:
                factorsFound.append(i)
                number /= i
            else:
                break
    return factorsFound


def solve_0005(number):
    '''
    1. Start with the highest number.
    2. Factor it to primes.
    3. Use each prime to divide all numbers in the list, that are on the right side of the number from 1).
    4. Move to the next position on the list and repeat steps 1-3.
    5. Execute 4) until the end of the list.
    '''
    multiplies = [i for i in range(number,0,-1)]
    smallestNumber = 1

    for iteration in range(len(multiplies)):        
        factors = factorToPrimes(multiplies[iteration]) 
        for factor in factors:
            for i in range(1+iteration,number):                
                if multiplies[i]%factor == 0:
                    multiplies[i] = int(multiplies[i]/factor)
        smallestNumber *= multiplies[iteration]          
    
    print('Smallest positive number evenly divisible by all of the numbers from 1 to {} is {}.'.format(number, smallestNumber))

solve_0005(10)
solve_0005(20)

