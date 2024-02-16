n=input()
l1=[]
s=pow(2,len(n))
for i in range(1,s):
    l=""
    j=0
    while(j<len(n)):
        if (i&(1<<j)):
            l+=n[j]
        j+=1
    l1.append(l)
print(sorted(l1))
