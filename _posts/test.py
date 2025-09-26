import sys

n = int(sys.stdin.readline())
res = []
li = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    li.append(a)

for i in range(n):
    cnt = 1
    for j in range(n):
        if li[j][0] > li[i][0] and li[j][1] > li[i][1]:
            cnt += 1
    res.append(cnt)

print(*res)

