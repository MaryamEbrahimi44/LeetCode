class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        missing = []

        for num in range(min(nums), max(nums) + 1):
            if num not in num_set:
                missing.append(num)

        return missing