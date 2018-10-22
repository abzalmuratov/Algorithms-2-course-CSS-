import random

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

print(n)
for i in range(n):
    print(a[i], end = " ")

'''-----------------------------------'''

m = int(input())
k = int(input())
a = []
n = random.randint(0, m)
for i in range(n):
    a.append(random.randint(k, 0))

print(n)
for i in range(n):
    print(a[i], end = " ")
