class Solution:
    def DivisibleByEight(self,s):
        #code here
        return (1 if (int(s[-3:])%8==0) else -1)
