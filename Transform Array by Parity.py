class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i,num in enumerate(nums):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        left=0
        right=len(nums)-1
        while left<right:
            while nums[left]==0 and left < right:
                left+=1
            while nums[right]==1 and left < right:
                right-=1
            if left < right:
                nums[left],nums[right]=nums[right],nums[left]
            right-=1
            left+=1

        return nums

            
        