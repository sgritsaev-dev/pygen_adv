with open('C:/Codes/goats.txt', 'r', encoding='utf-8') as goats, open('C:/Codes/answer.txt', 'w', encoding='utf-8') as answer:
    goats_lst = goats.read().split()
    clr_lst=[]
    majority=[]
    for el in goats_lst:
        if el!= 'COLOURS' and el != 'goat' and el!='GOATS':
                clr_lst.append(el)
    clr_set = set(clr_lst)

    for el in clr_set:
        result = clr_lst.count(el)*100//len(clr_lst)
        if result >  7:
            majority.append(el)
    majority.sort()
    for el in majority:
        answer.write(el+' goat\n')
