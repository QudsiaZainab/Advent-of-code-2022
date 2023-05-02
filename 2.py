list = []
for i in range(3):
  s = []
  s1 = input()
  s.append(s1)
  s2 = input()
  s.append(s2)
  list.append(s)
d = {'X':1,'Y':2,'Z':3}
score = 0
for i in list:
  if i[0] == 'A' and i[1] == 'X':
    score = score + 3
  elif i[0] == 'A' and i[1] == 'Y':
    score = score + 6
  elif i[0] == 'A' and i[1] == 'Z':
    score = score + 0
  elif i[0] == 'B' and i[1] == 'X':
    score = score + 0
  elif i[0] == 'B' and i[1] == 'Y':
    score = score + 3
  elif i[0] == 'B' and i[1] == 'Z':
    score = score + 6
  elif i[0] == 'C' and i[1] == 'X':
    score = score + 6
  elif i[0] == 'C' and i[1] == 'Y':
    score = score + 0
  elif i[0] == 'C' and i[1] == 'Z':
    score = score + 3
  score = score + d[i[1]]
print(score)