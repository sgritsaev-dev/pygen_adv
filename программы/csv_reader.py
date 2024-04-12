def read_csv():
    with open('C:\Codes\data.csv') as data:
            result=[]
            first_line = data.readline().strip().split(',')
            amount = len(data.readlines())
            data.seek(0)
            other_lines = data.readline().strip().split(',')
            for _ in range (amount):
                other_lines = data.readline().strip().split(',')
                result.append(dict(zip(first_line, other_lines)))
            return result