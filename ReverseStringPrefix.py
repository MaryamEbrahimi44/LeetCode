class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        newS=s[k-1::-1]+s[k:]
        return newS
