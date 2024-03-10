b= list(set(b))
        c = []
        d ={}
        for i in a:
            if(i not in d):
                d[i] =1
        for i in b:
            if(i in d):
                c.append(i)
        return c 
