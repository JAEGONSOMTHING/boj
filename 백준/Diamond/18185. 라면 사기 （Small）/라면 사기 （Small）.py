import re
import sys

n = int(sys.stdin.readline().rstrip())

mylist = list(map(int, sys.stdin.readline().split()))

c2 = 0
c1 = 0
count = 0
for d in mylist:
    if d == 0:
        c1 = 0
        c2 = 0
    else:
        n1 = min(c2, d)
        n2 = max(0, d - n1 - c1)
        count += 3 * d

        count -= min(c1+c2, d)
        c1 = n1
        c2 = n2


print(count)
