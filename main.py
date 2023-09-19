import time
print('\033[1;33mSCORE TABLE\033[0m')
print()
a = open('high.score', 'r')
c = []
d = []
while True:
  b = a.readline().strip()
  m = b.split()
  time.sleep(1)
  print(b)
  if b == '':
    break
  c.append(int(m[1]))
  d.append(m[0])
  
v = max(c)
w = c.index(v)
print(f'\033[32m{d[w]} has the highest score of {v}')
a.close()
