'''s = "1, 2, 4, 6"
list = s.split(' ')
print(list)'''

'''list = [10,20,30]
list.insert(1, "hello world!")
print(list)'''

'''list = [1,2,3,4,5,6,7,8,9]
print(list[-1])'''

def sum13(nums):
  if len(nums)==0:
    return 0
  else:
    new_nums = []
    for i in range(len(nums)-1):
        try:
            if nums[i]!=13:
                new_nums.append(nums[i])
            elif i != len(nums)-1:
                nums.pop(i+1)
        except:
            pass
    return sum(new_nums)/len(new_nums)

      
      

print(sum13([13]))