class Solution:
    def isHappy(self, n: int) -> bool:
        t = []
        
        def noncyclique(d):
            x = 0
            while d != 0:
                x = x + (d % 10) ** 2
                d = d // 10       
            if x == 1:
                return True
            else:
                if x in t:
                    return False
                else:
                    t.append(x)
                    return noncyclique(x) 
        
        return noncyclique(n)              

