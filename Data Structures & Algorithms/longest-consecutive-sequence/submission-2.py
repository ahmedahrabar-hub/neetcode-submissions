class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        x = 1
        t = []
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                x += 1
            else:
                t.append(x)
                x = 1
        t.append(x)    
        return max(t)
        