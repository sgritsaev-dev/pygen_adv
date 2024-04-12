with open('C:/Codes/input.txt') as input_file, open('C:/Codes/output1.txt', 'w') as output_file:
    amount = len(input_file.readlines())
    input_file.seek(0)
    for i in range (1, amount+1):
        output_file.write(str(i)+') ')
        output_file.write(input_file.readline())
