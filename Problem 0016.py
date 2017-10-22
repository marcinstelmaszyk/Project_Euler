'''
### Problem 0016 ### Power digit sum ###
What is the sum of the digits of the number 2^1000?
'''

def solve_0016(power):
    sum_digits = sum(int(digit) for digit in str(2**1000))

    print(sum_digits)

solve_0016(1000)
