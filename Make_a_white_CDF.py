t=int(input())
for i in range(1,t+1):
    n=int(input())
    l=input()
    i=0
    j=len(l)-1
    c=0
    c1=0
    while(i<len(l)):
        if l[i]=='B':
            c=i
            break
        else:
            i+=1
        
    while(j>0):
        if l[j]=='B':
            c1=j
            break
        else:
            j-=1
    print(j-i+1)
        
