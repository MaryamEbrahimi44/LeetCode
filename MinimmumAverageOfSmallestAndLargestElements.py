class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()

        minimum = float("inf")
        left, right = 0, len(nums) - 1

        while left < right:
            average = (nums[left] + nums[right]) / 2
            minimum = min(minimum, average)
            left += 1
            right -= 1

        return minimum