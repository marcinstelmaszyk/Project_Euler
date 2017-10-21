'''
### Problem 0017 ### Number letter counts ###
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''

LetterDictonary = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'
    }


def countWord(word):
    '''Return number of letters in a word.'''
    return len(word)

def countLetters(number):
    '''Recursive. Return a number of letters for number written out.'''
    if number/1000 >= 1:
        thousandsCount = countWord(LetterDictonary[int(number/1000)]) + countWord('thousand')
        if number%1000 > 0:
            return thousandsCount + countWord('and') + countLetters(number%1000)
        else:
            return thousandsCount
    if number/100 >= 1.0:
        hundredsCount = countWord(LetterDictonary[int(number/100)]) + countWord('hundred')
        if number%100 > 0:
            return hundredsCount + countWord('and') + countLetters(number%100)
        else:
            return hundredsCount    
    elif number/10 > 2:
        dozensCount = countWord(LetterDictonary[int(number/10)*10])
        if number%10 != 0:
            return dozensCount + countLetters(number%10)
        return dozensCount
    elif number/10 > 2:
        dozensCount = countWord(LetterDictonary[int(number/10)*10])
    elif number/10 > 1:
        return countWord(LetterDictonary[number])
    else:
        return countWord(LetterDictonary[number])

def solve_0017(startNum, endNum):
    total = 0
    for number in range(startNum, endNum+1):
        lettersInNumber = countLetters(number)
        total += lettersInNumber
        print(number, 'written out in words contains', lettersInNumber, 'letters.')
    print('Total number of letters used to write out all numbers from ({},{}): {}'.format(startNum, endNum, total))
    
solve_0017(1, 1000)