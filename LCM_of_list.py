l=[1,2,3,4,5]
k=max(l)
while(k>0):
    f=0
    for i in l:
        if k%i!=0:
            f=1
            k+=1
            break
    if f==0:
        break
print(k)
