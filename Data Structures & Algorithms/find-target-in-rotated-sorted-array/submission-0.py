class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1) find the pivot (index of the minimum)
        a = 0
        b = len(nums) - 1
        while a < b:
            n = (a + b) // 2
            if nums[n] > nums[b]:
                a = n + 1
            else:
                b = n
        pivot = a

        # 2) choose the half that can contain the target
        if nums[pivot] <= target <= nums[-1]:
            lo, hi = pivot, len(nums) - 1      # right sorted part
        else:
            lo, hi = 0, pivot - 1              # left sorted part

        # 3) normal binary search
        while lo <= hi:
            n = (lo + hi) // 2
            if nums[n] == target:
                return n
            elif nums[n] < target:
                lo = n + 1
            else:
                hi = n - 1
        return -1