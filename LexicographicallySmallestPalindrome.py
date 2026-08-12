class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left,right=0,len(s)-1
        s=list(s)
        while left<right:
            if ord(s[left])<ord(s[right]):
                s[right]=s[left]
            
            elif ord(s[left])>ord(s[right]):
                s[left]= s[right]
                
            left+=1
            right-=1
        return "".join(s)
        