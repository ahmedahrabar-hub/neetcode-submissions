from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        sorted_unique = sorted(count.keys())
        
        for card in sorted_unique:
            freq = count[card]
            if freq > 0:
                for i in range(groupSize):
                    if count[card + i] < freq:
                        return False
                    count[card + i] -= freq
        
        return True