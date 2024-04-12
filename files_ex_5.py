#txt = input()
with open('C:/Python_education/Codes/file.txt', 'r', encoding='utf-8') as text:
    print(*text.readlines()[-10:], sep='')