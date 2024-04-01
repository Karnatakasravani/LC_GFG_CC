class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        p=list(s.split())
        return len(p[-1])
