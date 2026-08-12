class Solution:
    def minimumFlips(self, n: int) -> int:
        s=bin(n)[2:]
        f=0
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                f+=2
            left+=1
            right-=1
        return f