# cook your dish here
t=int(input())
for _ in range(1,t+1):
    n=22
    
    ma=0
    l=[]
    for i in range(0,n):
        
        r,w=map(int,input().split())
        tot=r+(w*20)
        ma=max(ma,tot)
        l.append(tot)
    # print(l)
    for i in range(0,n):
        if l[i]==ma:
            print(i+1)
            break
    # print(ma)
        
