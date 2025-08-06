#Q1

num = int(input('enter num: '))
digit = int(input('enter digit: '))
def count(n):
    return len(str(n))

def reverse(n):
    return int(str(n)[::-1])

def hasDigit(n,d):
    return str(d) in str(n)

print('hasdigit: ', hasDigit(num,digit))
print('count:', count(num),'\nreverse: ', reverse(num))

'''
ojasmittal@pop-os ~/D/Code [1]> python3 q1.py
enter num: 2384658924450
enter digit: 1
hasdigit:  False
count: 13 
reverse:  544298564832
ojasmittal@pop-os ~/D/Code> python3 q1.py
enter num: 77777777777777777
enter digit: 7
hasdigit:  True
count: 17 
reverse:  77777777777777777
ojasmittal@pop-os ~/D/Code> python3 q1.py
enter num: 947437439
enter digit: 9
hasdigit:  True
count: 9 
reverse:  934734749
'''
