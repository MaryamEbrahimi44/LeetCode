class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i , n in enumerate(nums):
            c=target-n
            if c in seen:
                return [seen[c],i]
            seen[n]=i