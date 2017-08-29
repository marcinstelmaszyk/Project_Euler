'''
### Problem 0002 ### Even Fibonacci numbers ###
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

def get_Fibonacci():
    firstTerm = 1
    secondTerm = 2    
    yield firstTerm
    yield secondTerm
    while True:
        Fib_number = firstTerm + secondTerm
        yield Fib_number
        firstTerm, secondTerm = secondTerm, Fib_number    

def is_even(number):
    if number % 2:
        return False
    return True

def solve_0002(limit):
    sum = 0
    for num in get_Fibonacci():
        print(num, is_even(num))
        if (num < limit):
            if is_even(num):
                sum += num
        else:
            print('The sum of the even-valued terms in the Fibonacci sequence below {} is {}.'.format(limit, sum))
            return

solve_0002(4000000)