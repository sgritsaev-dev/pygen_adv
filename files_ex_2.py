from functools import reduce
with open('C:/Python_education/Codes/ledger.txt', 'r', encoding='utf-8') as ledger:
    txt = ledger.read().split()
    total = reduce(lambda x, y: int(x) + int(y), list(map(lambda x: x.strip('$'),txt)))
    print(total)