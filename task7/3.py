n = int(input())
str = input()
a = str.split()
for i in range(n) : a[i] = int(a[i])
l = 0
r = n
while(r - l > 0) :
    mid = (l + r) // 2
    if(a[mid] > a[l]): l = mid
    else: r = mid
print(a[l])
