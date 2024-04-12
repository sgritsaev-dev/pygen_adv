import string
with open ('C:/Codes/file.txt') as f:
    row = f.readline().split()
    lines=0
    words=0
    letters=0
    while len(row)>0:
        words+=len(row)
        if len(row)>0:
            lines+=1
        row = f.readline().split()
    f.seek(0)
    r = list(f.read())
    r_filtered = list(filter(lambda x: x in string.ascii_letters and not x.isspace(), r))
    letters = len(r_filtered)
    #print(r_filtered)


print('Input file contains:\n',
letters, 'letters\n',
words, 'words\n',
lines, 'lines')