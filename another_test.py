def alternate_upper(placeholder):
    for i in range(len(placeholder)):
        new_str = ''
        for integer in range(len(placeholder[i])):
            if integer%2==0:
                new_str+=placeholder[i][integer].upper()
            else:
                new_str+=placeholder[i][integer].lower()
        placeholder[i]=new_str
    return placeholder
 
print(alternate_upper(['cow','bat','sat']))