class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=[]
        r=Counter(nums)
        s=sorted(r.items(), key=lambda x:x[1], reverse=True)
        for j in range(k) :
            d.append(s[j][0])
        return d


        

            


        