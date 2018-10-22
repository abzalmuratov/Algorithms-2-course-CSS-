a = [] #1 operation
n = int(input()) #2 operation
for i in range(n) : #n operation
    a.append(int(input())) #1 operation
b = [] #1 operation
for i in range(len(a)): #[4n**2 + 4n] operation
    mn = 1000000 #1 operation
    index = -1 #1 operation
    for j in range(len(a)): #4n operation
        if mn > a[j] : #2 operation
            mn = a[j] #1 operation
            index = j #1 operation
    a.remove(a[index]) #1 operation 
    b.append(mn) #1 operation
    
print(b) #1 operation
#4n**2 + 5n + 5 [worst-case]
#O(n**2)
