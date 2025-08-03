#Q3

def romanToInt(n):
    roman = {
        "I":1, "V":5, "X":10,
        "L":50, "C":100,
        "D":500, "M":1000
    }
    
    total = 0
    i = 0
    while i < len(n):
        if i + 1 < len(n) and roman[n[i]] < roman[n[i+1]]:
            total += roman[n[i+1]] - roman[n[i]]
            i += 2
        else:
            total += roman[n[i]]
            i += 1
    return total

num = input("Enter Roman numeral: ")
print(romanToInt(num))

'''
ojasmittal@pop-os ~/D/Code (main)> python3 q3.py
Enter Roman numeral: MCMXIV
1914
ojasmittal@pop-os ~/D/Code (main)> python3 q3.py
Enter Roman numeral: MMMDCCCLXXXVIII
3888
ojasmittal@pop-os ~/D/Code (main) [1]> python3 q3.py
Enter Roman numeral: CD
400
'''