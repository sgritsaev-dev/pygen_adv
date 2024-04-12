
def dic_maker(amount,  dic={}, *country):
    x = ' '.join(country)
    dic.setdefault(x, amount)
with open('C:/Codes/population.txt') as population:
    countries={}
    general_spisok = population.readlines()
    population.seek(0)
    spisok = population.readline().split()
    while len(spisok)>0:
        dic_maker(int(spisok[-1]), countries, *spisok[:-1])
        spisok = population.readline().split()

    for el in countries:
        if el.startswith('G') and countries[el]>=500000:
            print(el, countries[el])
    #print(countries)