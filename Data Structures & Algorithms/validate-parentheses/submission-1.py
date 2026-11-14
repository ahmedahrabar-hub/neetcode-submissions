class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for x in s:
            if x in {"(","[","{"}:
                stack.append(x)
            else:
                if x==")":
                    if stack and stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                if x=="]":
                    if stack and stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
                if x=="}":
                    if stack and stack[-1]=="{":
                        stack.pop()
                    else:
                        return False   
        if stack==[]:
            return True
        else:
            return False 
            