class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]:
                continue
            else:
                nums[i+1]=0
                nums[i]=2*nums[i]

        j=0
        for i in range (len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        while j<len(nums):
            nums[j]=0
            j+=1
        return nums
                

        