#Q8

def parseTSV(r):
    rows = []
    for i in r:
        row = i.strip().split("\t")
        rows.append(tuple(row))
    return rows

def regList(l):
    l_new = l
    for i in range(len(l_new)):
        for j in range(len(l_new) - i - 1):
            if int(l_new[j][2]) > int(l_new[j+1][2]):
                l_new[j], l_new[j+1] = l_new[j+1], l_new[j]
    return l_new



with open("stud.tsv","r+") as f:
    lines = f.readlines()
    stud_set = regList(parseTSV(lines))
    young = []
    dep_freq = {}

    for i in stud_set:
        if i[4] in dep_freq:
            dep_freq[i[4]] += 1
        else:
            dep_freq[i[4]] = 1

        if int(i[3]) < 3:
            young.append(i[0] + " " + i[1])

    print("Students w/ yr < 3: ",young,"\nDep_Freq",dep_freq)

'''
ojasmittal@pop-os ~/D/C/q8 (main)> python3 q8.py
Students w/ yr < 3:  ['Anu Sharma', 'Rajat Sen'] 
Dep_Freq {'MME': 1, 'Biology': 2, 'CSEE': 3}
'''