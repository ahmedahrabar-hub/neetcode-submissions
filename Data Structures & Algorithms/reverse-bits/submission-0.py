class Solution:
    def reverseBits(self, n: int) -> int:
        s=0
        for i in range(32):
            if n!=0:
                x=n%2
                n=n//2
                s=s+2**(31-i)*x
            
        return s

      


        