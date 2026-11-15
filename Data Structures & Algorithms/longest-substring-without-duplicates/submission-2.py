class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        maxl=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            maxl=max(maxl,i-left+1)
        return maxl
 

                
        