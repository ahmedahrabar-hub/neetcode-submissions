class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        t=[]
        def construction(current,op,cl):
            if len(current)==(n*2):
                t.append(current)
                return
            
            
            if op<n:
                construction(current + "(" , op+1 ,cl)
            if cl<op:
                construction(current + ")" , op , cl+1)
        construction("",0,0)
        return t

            

        


        