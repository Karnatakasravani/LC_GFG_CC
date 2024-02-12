def Countpair (self, arr, n, sum) : 
        #Complete the function
        arr.sort()
        i=0
        j=len(arr)-1
        # s=0
        cnt=0
        while(i<j):
            if arr[i]+arr[j]==sum:
                cnt+=1
                i+=1
                j-=1
            elif arr[i]+arr[j]>sum:
                j-=1
            else:
                i+=1
        if cnt==0:
            return -1
        return cnt
