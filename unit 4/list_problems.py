import math
def average_len(l):
    total = 0
    for element in l:
        total+=len(element)
    return total/len(l)

def pal_count(l):
    count=0
    for element in l:
        if element==element[::-1]:
            count+=1
    return count

def concatonate_str(l):
    string = ''
    for element in l:
        string += element
        string += ' '
    return string

def vowel_count(l):
    vowels = 'aeiou'
    dictionary = {}
    for element in l:
        count = 0
        for i in range(len(element)):
            if element[i] in vowels:
                count+=1
        new_dic = {element: count}
        dictionary.update(new_dic)
    return dictionary

def alternate_upper(l):
    for i in range(len(l)):
        new_str = ''
        for intager in range(len(l[i])):
            if intager%2==0:
                new_str+=l[i][intager].upper()
            else:
                new_str+=l[i][intager].lower()
        l[i]=new_str
    return l

def pos_neg(l):
    pos_list = []
    neg_list = []
    for element in l:
        if element>0:
            pos_list.append(element)
        elif element<0:
            neg_list.append(element)
    return pos_list, neg_list

def fibonacci(sequence):
    if len(sequence) < 3:
        return False

    for i in range(2, len(sequence)):
        if sequence[i-2] + sequence[i-1] != sequence[i]:
            return False
    return True

def square_roots(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(round(math.sqrt(list[i]),0))
    return new_list

def running_average(list):
    total = 0
    new_list = []
    for i in range(1,len(list)+1):
        total +=list[i-1]
        new_list.append(total/i)
    return new_list

def cons_pair(list):
    for i in range(len(list)-1):
        if list[i+1] - list[i]==1:
            return "diff of 1"
    return "no diff of 1"

#print(average_len(['asdf','asd','asdfg']))
#print(pal_count(['abcba','asdfg','123321']))
#print(concatonate_str(['hello', 'world']))
#print(vowel_count(['aedfhf','back']))
#print(alternate_upper(['abc', 'def']))
#print(pos_neg([1,-3,6,-3,9]))
#print(fibonacci([1,1,2,3,5,8,13]))
#print(square_roots([4,9,16,23,25]))
#print(running_average([2,4,6]))
#print(cons_pair([1,2,5,7,9]))