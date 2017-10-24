'''
### Problem 0006 ### Sum square difference ###
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def D_n(number):
    '''
    Recursive function
    Returns difference D_n = [Sum(i)]^2 - Sum(i^2) = D_(n-1) + (n-1)*n^2
    '''
    D_1 = 0

    if number == 1:
        return D_1
    else:
        return D_n(number-1) + (number-1)*number*number   

def solve_0006(number):    
    difference = D_n(number)
    print('The difference for the first {} natural numbers is {}'.format(number, difference))

solve_0006(100)
