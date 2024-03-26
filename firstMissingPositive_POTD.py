class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = {}
        for i in nums:
            if i not in l:
                l[i]=1

        for i in range(1,len(nums)+2):
            if i not in l:
                return i
        return -1
