t=int(input())
for _ in range(1,t+1):
    n=int(input())
    s=""
    if n>52:
        s+=chr((n-(2*26))+96)
        s+='zz'
    elif n<=28:
        s+='aa'
        s+=chr((n)+(96-2))
    else:
        a=n-26
        b=a-1
        s+='a'
        s+=chr(b+96)
        s+='z'
    print(s)
