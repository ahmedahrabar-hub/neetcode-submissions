class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            s=s^i^nums[i]
        s=s^(len(nums))
        return s

        