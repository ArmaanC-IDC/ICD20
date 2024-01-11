import time
'''list = [i for i in range(1,101) if i%2==0 if i>=50 or i<=20]
print(list)'''


'''def xyz_there(str):
  for i in range(0,len(str)-2):
    if str[i:i+3] == 'xyz':
      return True
    else:
      pass
  return False

print(xyz_there('abcxyz'))'''


def get_prime_numbers():
  start = int(input("Start: "))
  stop = int(input("Stop: "))
  list = [i for i in range(start,stop+1)]
  prime_list = [i for i in range(start,stop+1)]
  for list_element in list:
      if list_element==4:
          prime_list.remove(4)
      for i in range(2,list_element//2):
          if list_element%i==0:
              try:
                prime_list.remove(list_element)
                print(f"{list_element} by {i}")
              except ValueError:
                  pass
  return prime_list

def palindrome_checker(str):
  palindrome = True
  for i in range(len(str)-1):
    if str[i] == str[len(str)-1-i]:
      pass
    else:
      palindrome = False
  return palindrome

def fibonacci(l):
  sequence = [1,1]
  for i in range(2,l):
    sequence.append(sequence[i-2] + sequence[i-1])
  return sequence
  
print(get_prime_numbers())
# print(palindrome_checker("aabcbbaa"))
# print(fibonacci(10))   