class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        i=0
        result=[]
        while i < len(nums):
            count=1
            while  i+1 < len(nums) and nums[i]==nums[i+1] :
                count+=1
                i+=1
            for j in range(min(k,count)):
                result.append(nums[i])
            i+=1
        
            
        return result
            
        