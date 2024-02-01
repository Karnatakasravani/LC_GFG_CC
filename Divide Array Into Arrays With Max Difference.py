class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        l=[]
        for i in range(0,len(nums),3):
            if abs(nums[i]-nums[i+2])<=k:
                l.append(list((nums[i],nums[i+1],nums[i+2])))
            else:
                l=[]
                break
        return l

        
