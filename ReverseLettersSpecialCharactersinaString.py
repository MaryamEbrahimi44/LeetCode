class Solution:
    def reverseByType(self, s: str) -> str:
        s=list(s)
        left,right=0,len(s)-1
        while left<right:
            if s[left].isalpha() and s[right].isalpha():
                s[left],s[right]=s[right],s[left]
                right-=1
                left+=1
            elif s[left].isalpha() and  not s[right].isalpha():
                
                right-=1
            elif not s[left].isalpha() and s[right].isalpha():
                left+=1
            else:  
                right-=1
                left+=1
        left,right=0,len(s)-1
        while left<right:
            if not s[left].isalpha() and not s[right].isalpha():
                s[left],s[right]=s[right],s[left]
                right-=1
                left+=1
            elif s[left].isalpha() and  not s[right].isalpha():
                left+=1
            elif not s[left].isalpha() and s[right].isalpha():
                right-=1
            else:  
                right-=1
                left+=1
    

        return "".join(s)
        