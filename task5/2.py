a = [-1, 2, 1, 4] #1 operation
sum = 0 #1 operation 
for i in range(len(a)): #3n operation
    if a[i] > 0: #2 operation
        sum += a[i] #1 operation
print(sum) #1 operation

#3n + 3 worst-case
#O(n*log(n))
