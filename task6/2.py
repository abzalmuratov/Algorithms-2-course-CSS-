f = input()
a = f.split()
n = len(a)
avg = 0
for i in range(n): a[i] = int(a[i])
sorted(a)
for i in range(1, n): a[i] += a[i - 1]
for i in range(n): avg += a[i]
print(avg / n)
    
