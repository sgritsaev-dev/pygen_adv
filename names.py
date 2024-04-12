from random import sample as s
with open('C:/Codes/first_names.txt') as first, open('C:/Codes/last_names.txt') as last:
    random_names = s(list(map(lambda x: x.strip(), first.readlines())), 3)
    random_surnames = s(list(map(lambda x: x.strip(), last.readlines())), 3)
    variants = dict(zip(random_names, random_surnames))
    for el in variants:
        print(el, variants[el])