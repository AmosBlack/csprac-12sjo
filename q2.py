# Q2

number = int(input('enter num: '))

def generateFactors(num):
    factors = []
    div = 1
    while div < num:
        if num % div == 0:
            factors.append(div)
        div += 1
    return factors

def isPrimeNo(num):
    if len(generateFactors(num)) < 2:
        return 'Prime'
    return 'Not Prime'

def isPerfectNo(num):
    if sum(generateFactors(num)) == num:
        return 'Perfect'
    return 'Not Perfect'

print(isPerfectNo(number), isPrimeNo(number))

'''
ojasmittal@pop-os ~/D/Code> python3 q1.py
enter num: 56
Not Perfect Not Prime
ojasmittal@pop-os ~/D/Code> python3 q1.py
enter num: 6
Perfect Not Prime
ojasmittal@pop-os ~/D/Code> python3 q1.py
enter num: 17
Not Perfect Prime
'''