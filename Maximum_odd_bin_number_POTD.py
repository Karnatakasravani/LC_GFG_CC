class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=s.count('1')
        zeroes=s.count('0')
        ne=""
        for i in range(ones-1):
            ne+='1'
        new='0'*zeroes+'1'
        return ne+new
