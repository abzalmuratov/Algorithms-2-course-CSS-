w = int(input())
n = int(input())
wa = input()
ca = input()
wei = wa.split()
cal = ca.split()
a = []
for i in range(n): a.append(int(cal[i]) / int(wei[i]))
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            wei[i], wei[j] = wei[j], wei[i]
            
i = 0
sumx = 0
while(w != 0):
    weight = int(wei[n - i - 1]) 
    if w >= weight:
        w -= weight
        sumx += weight * a[n - i - 1]
    else :
        weight -= w
        sumx += w * a[n - i - 1] 
        break
    i = i + 1
print(sumx)
