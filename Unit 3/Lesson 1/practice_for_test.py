def make_chocolate(small, big, goal):
  while True:
    goal -= 5
    big-= 1
    if goal<5:
      break
    elif big<1:
      break
  return goal

print(make_chocolate(4, 1, 9))