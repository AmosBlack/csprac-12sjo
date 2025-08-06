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

    