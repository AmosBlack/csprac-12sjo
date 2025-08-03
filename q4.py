#Q4

num = int(input('enter decimal num: '))
con = input('B:binary H:Hex O:Octal\nenter conversion:')

def B(n):
    f = n 
    binary = ''
    while f >= 1:
        binary = binary + str(f%2)
        f = f//2 
    return binary[::-1]

def H(n):
    f = n 
    hex = ''
    j = ord('A')

    while f >= 1:
        digit = f%16
        if digit > 9:
            digit = chr(j + digit - 10)
        hex = hex + str(digit)
        f = f//16
 
    return hex[::-1]


def O(n):
    f = n 
    octal = ''
    while f >= 1:
        octal = octal + str(f%8)
        f = f//8
    return octal[::-1]

def joinList(list):
    string = ''
    for i in list:
        string = string + i
    return string
dict = {
    'B': B(num),
    'H': H(num),
    'O': O(num)
}

print(joinList(dict[con]))

'''
ojasmittal@pop-os ~/D/Code> python3 q4.py
enter decimal num: 999
B:binary H:Hex O:Octal
enter conversion:H
3E7
ojasmittal@pop-os ~/D/Code> python3 q4.py
enter decimal num: 999
B:binary H:Hex O:Octal
enter conversion:O
1747
ojasmittal@pop-os ~/D/Code> python3 q4.py
enter decimal num: 999
B:binary H:Hex O:Octal
enter conversion:B
1111100111
'''