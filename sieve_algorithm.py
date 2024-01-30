n=10
prime = [True ]*(n+1)
p = 2
while (p * p <= n):
    for i in range(p * p, n+1, p):
         if (prime[p] == True):
            prime[i] = False
    p += 1
c=0
for p in range(2, n+1):
    if prime[p]:
        c+=1
        print(p,end=" ")
print(c)
