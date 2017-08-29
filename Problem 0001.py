'''
### Problem 0001 ### Multiples of 3 and 5 ###
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def generate_multiples(number, limit):
    '''Return a set of a number's multiples.'''
    multiples = set()
    for num in range(number, limit, number):
        multiples.add(num)        
    return multiples


def solve_0001(numbers, limit):
    multiples = set()
    for number in numbers:
        multiples |= generate_multiples(number, limit)   
    sum = 0
    for num in list(multiples):
        sum += num    
    print('Sum of all the multiples of 3 or 5 below {} is {}.'.format(limit, sum))


solve_0001(numbers=[3,5], limit=1000)