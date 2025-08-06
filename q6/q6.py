#Q6

blob = "Neither apple nor pine are in pineapple. Boxing rings are square.\nWriters write, but fingers dont fing.Overlook and oversee are opposites.\nA house can burn up as it burns down. An alarm goes off by going on. \n"

def readLines(file):
    file.seek(0)
    return file.readlines()

def dispLine(n,file):
    return readLines(file)[n-1]

def freqTrain(file):
    f.seek(0)
    text = file.read()
    text_break = text.split(" ")
    train = {}

    for i in text_break:
        if i[0] == '\n':
            continue
        elif i[0].lower() not in train:
            train[i[0].lower()] = 1
        else:
            train[i[0].lower()] += 1
    
    print(train)



with open("blob.txt", "a+") as f:
    f.write(blob)         
    lines = readLines(f)

    f.write("Apple seeds contain hydrogen cyanide. That stuff can kill you")                                     
    
    lines = readLines(f)
    for i in range(len(lines)):
        print(i+1,": ", lines[i])

    print("Last line-")
    print(lines[-1])
    print("10th char onwards-")
    print(lines[0][10::])

    index = int(input("Enter line no: ")) - 1
    print(dispLine(index,f))

    freqTrain(f)

'''
ojasmittal@pop-os ~/D/C/q6 (main)> python3 q6.py
1 :  Neither apple nor pine are in pineapple. Boxing rings are square.

2 :  Writers write, but fingers dont fing.Overlook and oversee are opposites.

3 :  A house can burn up as it burns down. An alarm goes off by going on. 

4 :  Apple seeds contain hydrogen cyanide. That stuff can kill youNeither apple nor pine are in pineapple. Boxing rings are square.

5 :  Writers write, but fingers dont fing.Overlook and oversee are opposites.

6 :  A house can burn up as it burns down. An alarm goes off by going on. 

7 :  Apple seeds contain hydrogen cyanide. That stuff can kill you
Last line-
Apple seeds contain hydrogen cyanide. That stuff can kill you
10th char onwards-
ple nor pine are in pineapple. Boxing rings are square.

Enter line no: 2
Neither apple nor pine are in pineapple. Boxing rings are square.

{'n': 3, 'a': 16, 'p': 4, 'i': 4, 'b': 10, 'r': 2, 's': 6, 'w': 2, 'f': 4, 'd': 4, 'o': 8, 'h': 4, 'c': 8, 'u': 2, 'g': 4, 't': 2, 'k': 2, 'y': 2}
'''
    