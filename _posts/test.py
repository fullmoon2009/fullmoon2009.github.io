import sys
from collections import deque

d = deque()
g = deque()
res = deque()
n = int(sys.stdin.readline())

for i in range(n):
    d.append(int(sys.stdin.readline()))

flag = True
cnt = 0

while len(d) > 0:
    if flag == True:
        g.append(1)
        res.append("+")
        i = 2
        flag = False

    if not g:
        if i < n + 1:
            g.append(i)
            res.append("+")
            i += 1

    if g[-1] == d[0]:
        g.pop()
        d.popleft()
        res.append("-")
        continue

    if i < n + 1:
        g.append(i)
        res.append("+")
        i += 1

    else:
        cnt += 1
        print("NO")
        break
    
if cnt == 0:
    print("\n".join(res))
    

    
