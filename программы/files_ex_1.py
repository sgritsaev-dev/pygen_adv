txt = input()
with open(txt, 'r', encoding='utf-8') as input:
    amount = len(input.readlines())
    print(amount)