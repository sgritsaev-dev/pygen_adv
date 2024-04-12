with open('C:/Python_education/Codes/logfile.txt', 'r', encoding='utf-8') as logs_file, open('C:/Python_education/Codes/output.txt', 'w', encoding='utf-8') as output:
    amount = len(logs_file.readlines())
    logs_file.seek(0)
    for _ in range (amount):
        logs = logs_file.readline().strip().split(', ')
        time_out_raw = logs[-1].split(':')
        time_in_raw = logs[-2].split(':')
        out_min = int(time_out_raw[0])*60 + int(time_out_raw[1])
        in_min = int(time_in_raw[0])*60 + int(time_in_raw[1])
        if (out_min-in_min)>=60:
            output.write(logs[0]+'\n')

