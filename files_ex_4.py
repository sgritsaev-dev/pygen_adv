with open('C:/Python_education/Codes/words.txt', 'r', encoding='utf-8') as words:
    maxlen=0
    w = words.read().split()
    for el in w:
        if len(el)>=maxlen:
            maxlen=len(el)
    for el in w:
        if len(el)==maxlen:
            print(el)