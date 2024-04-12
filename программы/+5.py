with open('C:/Codes/class_scores.txt', 'r', encoding='utf-8') as old_scores, open('C:/Codes/class_scores_new.txt', 'w', encoding='utf-8') as new_scores:
    amount = len(old_scores.readlines())
    old_scores.seek(0)
    for i in range (amount):
        pupil = old_scores.readline().split()
        #print(pupil)
        if len(pupil)>0 and int(pupil[-1])<=94:
            pupil[-1]=' '+str(int(pupil[-1]) + 5)+'\n'
            new_scores.writelines(pupil)
        elif len(pupil)>0 and int(pupil[-1])>94:
            pupil[-1]=' '+'100'+'\n'
            new_scores.writelines(pupil)
            
# Test comment
    
