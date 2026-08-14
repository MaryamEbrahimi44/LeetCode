class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        seen=set(nums)
        ans=-1
        for num in nums:
            if num>0 and -num in seen:
                ans=max(ans,num)
        return ans
       

        