class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            # l.append(nums.count(nums[i]))
        p=max(d.values())
        s=0
        for i in d.values():
            if i==p:
                s+=i
        return s
