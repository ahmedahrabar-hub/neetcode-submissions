class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        n=len(digits)
        for i in range(len(digits)):
            s=s+digits[i]*(10**(n-i-1))

        return list(str(s+1))
            
        