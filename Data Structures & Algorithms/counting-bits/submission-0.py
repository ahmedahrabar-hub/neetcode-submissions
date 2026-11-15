class Solution:
    def countBits(self, n: int) -> List[int]:
        t=[]
        for d in range(n+1):
            t.append(bin(d).count("1"))
        return t


        