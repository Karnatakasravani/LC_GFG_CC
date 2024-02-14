class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(len(pos)):
            nums[2*i]=pos[i]
        for i in range(len(neg)):
            nums[2*i+1]=neg[i]
        return nums
        
