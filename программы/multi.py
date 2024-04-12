names = [input('text') for n in range (int(input('num')))]
#names = ['answer.txt', 'output1.txt']
with open('output.txt', 'a') as output:
    for name_file in names:
        with open(name_file) as name:
            output.write(name.read().strip())


#print(names)