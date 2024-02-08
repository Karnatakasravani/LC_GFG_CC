class Solution:
    def addDigits(self, num: int) -> int:
        # s=0
        while(num>9):
            s=0
            while(num):
                d=num%10
                s+=d
                num=num//10
            num=s
        return num
        
