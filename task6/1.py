cent = float(input())
c = input()
a = c.split()
n = len(a)
cent *= 100

cnt = 0
coin = []
freq = []
for i in range(n):
    mx = int(a[n - i - 1])
    if(cent >= mx):
        cnt = cent // mx
        coin.append(mx)
        freq.append(cnt)
        cent %= mx
    if(cent == 0):
        print(coin)
        print(freq)
        break

if(cent != 0): print("-1")
    
