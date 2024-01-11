l1 = input("line 1: ")
l2 = input("line 2: ")
l3 = input("line 3: ")
l4 = input("line 4: ")

list1 = list(l1.split(' '))
list2 = list(l2.split(' '))
list3 = list(l3.split(' '))
list4 = list(l4.split(' '))

for i in range(len(list1)):
    list1[i] = int(list1[i])
    list2[i] = int(list2[i])
    list3[i] = int(list3[i])
    list4[i] = int(list4[i])

c1_sum = list1[0]+list2[0]+list3[0]+list4[0]
c2_sum = list1[1]+list2[1]+list3[1]+list4[1]
c3_sum = list1[2]+list2[2]+list3[2]+list4[2]
c4_sum = list1[3]+list2[3]+list3[3]+list4[3]

if sum(list1)==sum(list2)==sum(list3)==sum(list4)==c1_sum==c2_sum==c3_sum==c4_sum:
    print('magic')
else:
    print('not magic')
