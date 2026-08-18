class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result=[]
        left,right=0,len(nums)-1
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                result.append(nums[left]**2)
                left+=1
            else:
                result.append(nums[right]**2)
                right-=1
        return result[::-1]