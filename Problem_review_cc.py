# cook your dish here
t=int(input())
for _ in range(1,t+1):
    n=int(input())
    l=list(map(int,input().split()))
    for i in l:
        if i<=4:
            print("NO")
            break
    else:
        print("YES")
