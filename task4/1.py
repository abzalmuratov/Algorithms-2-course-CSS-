def rec(x) :
    if x == 0 or x == 1 or x == 2: return 1
    return rec(x - 1) + rec(x - 2) + rec(x - 3)

def func(x) :
    a = []
    for i in range(x + 1) : a.append(0);
    a[0] = a[1] = a[2] = 1
    for i in range(3, x + 1) :
        a[i] = a[i - 1] + a[i - 2] + a[i - 3];
    return a[x]
n = int(input())
print("first")
print(rec(n))
print("second")
print(func(n))
