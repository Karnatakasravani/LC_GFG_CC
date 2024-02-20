n=int(input())
l=list(map(int,input().split()))
s=0
pre=[]
for i in range(len(l)):
    s+=l[i]
    pre.append(s)
for i in range(len(pre)):
    if pre[i-1]==pre[n-1]-pre[i]:
        print(i)
        break
else:
    print(-1)
