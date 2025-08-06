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
    
    train_list = list(train.items())
    for i in train_list:
        print("Words beginning with ", i[0], ": ", i[1])


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

4 :  Apple seeds contain hydrogen cyanide. That stuff can kill you
Last line-
Apple seeds contain hydrogen cyanide. That stuff can kill you
10th char onwards-
ple nor pine are in pineapple. Boxing rings are square.

Enter line no: 1
Apple seeds contain hydrogen cyanide. That stuff can kill you
Words beginning with  n :  2
Words beginning with  a :  8
Words beginning with  p :  2
Words beginning with  i :  2
Words beginning with  b :  5
Words beginning with  r :  1
Words beginning with  s :  3
Words beginning with  w :  1
Words beginning with  f :  2
Words beginning with  d :  2
Words beginning with  o :  4
Words beginning with  h :  2
Words beginning with  c :  4
Words beginning with  u :  1
Words beginning with  g :  2
Words beginning with  t :  1
Words beginning with  k :  1
Words beginning with  y :  1
'''
    