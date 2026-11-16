class Solution:
    def findMin(self, nums: List[int]) -> int:
        a=0
        b=len(nums)-1
        while a<b:
            n=(a+b)//2
            if  nums[n]>nums[b]:
                a=n+1
            else:
                b=n
        return nums[a]

        