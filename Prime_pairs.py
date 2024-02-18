def isprime(N):
    cnt=0
    for i in range(1,N):
        if N%i==0:
            cnt+=1
    if cnt==1:
        return True
    return False
n=10
l=[]
for i in range(1,n):
    if isprime(i):
        l.append(i)
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==n:
            print(l[i],l[j])
# print(l)
