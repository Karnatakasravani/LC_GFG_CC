class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # return 0
        cnt=0
        d={}
        for i in stones:
            if i in jewels:
                cnt+=1
        return (cnt)
