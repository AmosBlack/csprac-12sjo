#Q11

def applicants(appl):
    return (len(appl) - 1)

def score(list):
    score = 0
    for i in range(len(list)):
        if i > 1:
            score += int(list[i])
    return score


def n_top(d,n):

    l = list(d.items())
    names = []
    for i in range(len(l)):
        for j in range(len(l)-i-1):
                if l[j][1] > l[j+1][1]:
                    l[j],l[j+1] = l[j+1],l[j]

    l.reverse()

    for j in range(len(l)):
        if j < n:
            names.append(l[j][0])
    
    return names

ranks = {}

with open("placement.csv","r") as f:
    appl = f.readlines()

    for i in range(len(appl)):
        
        data = appl[i].split(',')

        for j in data:
            print(j, end = " ")
        print()
        
        
        if i > 0:
            ranks[data[1]] = score(data)

    print("no of applicants: ", applicants(appl))
    num = int(input("filter length: "))
    print("top",num,"applicants: ", n_top(ranks,num))

'''
sample csv
SNO,NAME,MARKS1,MARKS2,MARKS3,MARKS4,MARKS5
1,Aarav,4,5,3,4,5
2,Diya,3,2,4,5,3
3,Vihaan,5,5,5,4,5
4,Isha,2,3,4,2,1
5,Reyansh,4,4,4,4,4
6,Myra,1,2,3,2,1

ojasmittal@pop-os ~/D/C/q11 (main)> python3 q11.py
SNO NAME MARKS1 MARKS2 MARKS3 MARKS4 MARKS5
 
1 Aarav 4 5 3 4 5
 
2 Diya 3 2 4 5 3
 
3 Vihaan 5 5 5 4 5
 
4 Isha 2 3 4 2 1
 
5 Reyansh 4 4 4 4 4
 
6 Myra 1 2 3 2 1
 
no of applicants:  6
filter length: 4
top 4 applicants:  ['Vihaan', 'Aarav', 'Reyansh', 'Diya']
'''

    

