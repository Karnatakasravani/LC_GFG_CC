class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=sorted(nums)
        i=0
        while(i!=(i+1)):
            if l[i]==l[i+1]:
                return l[i]
            else:
                i+=1
