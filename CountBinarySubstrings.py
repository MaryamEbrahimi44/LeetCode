class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_grp=0
        curr_grp=1
        r=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curr_grp+=1
            else:
                r+=min(curr_grp,prev_grp)
                prev_grp=curr_grp
                curr_grp=1
        r+=min(curr_grp,prev_grp)
        return r