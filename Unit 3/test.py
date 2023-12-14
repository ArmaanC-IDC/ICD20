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

for i in range(1, 101):
    print(f"{i} - /n {i**2}")