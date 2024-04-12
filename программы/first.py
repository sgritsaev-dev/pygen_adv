from functools import reduce
import string
with open('C:/VS code pets/edu/nums.txt') as l:
    sum=0
    amount = len(l.readlines())
    l.seek(0)
    for _ in range (amount):
        spisok = l.readline().split()
        for el in spisok:
            if el.isdigit():
                sum+=int(el)
            elif not el.isdigit() and len(el)>1:
                x=''
                for c in el:
                    if not c.isdigit():
                        x +=' '
                    if c.isdigit():
                        x +=c
                for el in x.split():
                    sum+=int(el)
        
    print(sum)   
