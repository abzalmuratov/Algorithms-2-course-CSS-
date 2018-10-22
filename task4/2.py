def euklid(a, b):
    if b == 0 :
        return a
    else :
        return euklid(b, a % b)

import time
a = int(input())
b = int(input())
stat = time.localtime(time.time())
i = min(a, b);
while(i) :
    if(a % i == 0 and b % i == 0): break
    i -= 1
print(i)
stat1 = time.localtime(time.time())
print(abs(stat1[5] - stat[5]))

print("Euklid's algo")
stat = time.localtime()
x = euklid(a, b)
stat1 = time.localtime()
print(abs(stat1[5] - stat[5]))
