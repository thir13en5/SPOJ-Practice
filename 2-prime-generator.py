import math
t = int(input())
a = 0
for t_i in range(t):
    m, n = map(int, input().split())
    for j in range(m,n+1):
        for k in range(2, math.sqrt(n)+1):
            if j%k == 0:
                a = 1
                break
        if a == 0 and j != 1:
            print(j)
            a = 0
        print("")