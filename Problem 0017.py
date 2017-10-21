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
    15 : 'fifteen',
    40 : 'forty'
    }


def countWord(word):
    return len(word)


def countLetters(number):

    if number/100 >= 1.0:
        hundredsCount = countWord(LetterDictonary[int(number/100)]) + countWord('hundred')
        if number%100 > 0:
            return hundredsCount + countWord('and') + countLetters(number%100)
        else:
            return hundredsCount
    elif number/10 > 2:
        dozensCount = countWord(LetterDictonary[int(number/10)*10])
        return dozensCount + countLetters(number%10)
    elif number/10 > 1:
        return countWord(LetterDictonary[number])
    else:
        return countWord(LetterDictonary[number])
        






def solve_0017(number):
    print(countLetters(number))




solve_0017(5)
