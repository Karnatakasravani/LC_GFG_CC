t=int(input())
for _ in range(1,t+1):
    n=int(input())
    l=list(map(int,input().split()))
    su=0
    pre=[]
    flag=0
    for i in range(0,n):
        su+=l[i]
        pre.append(su)
    for i in range(len(pre)):
        if pre[i-1]==pre[n-1]-pre[i]:
            print(i)
            flag=1
            break
    if flag==0:
        print(-1)

              
    
