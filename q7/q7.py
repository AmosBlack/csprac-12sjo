#Q7

def isVowel(l):
    blob = []
    for i in l:
        for j in i.split(' '):
            if j[0].lower() in "aeiou" and j != '\n':
                blob.append(j + " ")
    with open("file2.txt","w") as f:
        f.writelines(blob)


with open("file1.txt", "r") as f:
    lines = f.readlines()
    isVowel(lines)

'''
file1
I saw my name written on the foggy mirror. I live alone.
The dog barked at the fridge again. We don’t have a dog.
Someone keeps putting socks in the freezer. They’re always warm when I take them out.
The TV turned on by itself last night. It was just static, but it laughed once.
My phone rang. It was my number. I answered. It was me.
I watered the plant yesterday. Today it moved closer to my bed.
There’s a birthday cake in the oven. Nobody has a birthday.
I opened the door and saw myself walking in.
Every night, my toothbrush is wet before I use it.
The fan spins even when it’s unplugged.
file2
I on I alone.
at again. a in always I out.
on itself It it once.
It I answered. It I it a in oven. a I opened and in.
Every is I use it.
even it’s unplugged. 
'''