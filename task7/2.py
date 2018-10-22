n = int(input())
str = input()
a = str.split()
for i in range(n) : a[i] = int(a[i])
l = 0
r = n
while(r - l > 0) :
    mid = (l + r) // 2
    if ((mid == 0 or a[mid - 1] <= a[mid]) and
            (mid == n - 1 or a[mid + 1] <= a[mid])):
                print(a[mid])
                break

    elif (mid > 0 and a[mid - 1] > a[mid]): r = mid - 1
    else: l = mid + 1

print(a[r])