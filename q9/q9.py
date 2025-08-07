#Q9

def find_longest_word(f):
    return f[max(list((f.keys())))]

def filter_long_words(f,n):
    words = []
    for j in f.items():
        if j[0] > n:
            words.extend(j[1])
    return words

with open("myfile.txt","r") as f:
    words = f.read().split(" ")
    
    hist = {}
    freq = {}
    common_word = []
    max_len = 0        
    
    #hist
    for i in words:
        if i in hist:
            hist[i] += 1
        else:
            hist[i] = 1
    #freq
    for k in words:
        if len(k) in freq and k not in freq[len(k)]:
            freq[len(k)].append(k)
        elif len(k) not in freq:
            freq[len(k)] = [k]

    #comm word
    for j in hist.items():
        if j[1] > max_len:
            max_len = j[1]
            common_word = [j[0]]
        elif j[1] == max_len:
            common_word.append(j[0])

    print("words: ", sum(list(hist.values())))
    print("distinct words: ", len(hist))
    print("most common words: ", common_word)
    print("longest words: ",find_longest_word(freq))
    num = int(input("enter filter length: "))
    print("filtered words: ",filter_long_words(freq,num))

'''
file - shadow light mirror shadow light door forest mirror apple night shadow light fog light shadow apple forest fog mirror light shadow door apple night fog apple door night mirror forest shadow light forest light mirror apple shadow fog door night
ojasmittal@pop-os ~/D/C/q9 (main)> python3 q9.py
words:  40
distinct words:  8
most common words:  ['shadow', 'light']
longest words:  ['shadow', 'mirror', 'forest']
enter filter length: 4
filtered words:  ['shadow', 'mirror', 'forest', 'light', 'apple', 'night']
'''
    
