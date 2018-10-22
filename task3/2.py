n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

mn = 3600000
for i in range(0, n):
    for j in range(1, n):
        for k in range(2, n):
            x = a[i] + a[j] + a[k]
            if(x < mn and i != j and j != k): mn = x;

print(mn)

sorted(a)
print(a[0] + a[1] + a[2])
