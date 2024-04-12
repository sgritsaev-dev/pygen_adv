with open('C:/Python_education/Codes/grades.txt', 'r', encoding ='utf-8') as grades:
    total=0
    amount = len(grades.readlines())
    grades.seek(0)
    for _ in range (amount):
        line = grades.readline().strip().split()
        if int(line[-1])>=65 and int(line[-2])>=65 and int(line[-3])>=65:
            total+=1
    print(total)

        