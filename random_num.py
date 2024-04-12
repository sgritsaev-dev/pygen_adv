from random import sample as s
with open('random.txt', 'w', encoding='utf-8') as output:
    print(*s(range(111,778), 25), file=output, sep='\n')

