import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)
        if n % groupSize != 0:
            return False
        cnts = Counter(hand)
        cnts = [[x,y] for x, y in cnts.items()]
        heapq.heapify(cnts)
        k = n // groupSize
        
        for group in range(k):
            usedheap = []
            for _ in range(groupSize):
                if _ == 0:
                    x, freq = heapq.heappop(cnts)
                    if freq > 1:
                        usedheap.append([x, freq - 1])
                    continue
                if cnts:
                    newx, freq = heapq.heappop(cnts)
                else:
                    return False
                if newx == x + 1:
                    if freq > 1:
                        usedheap.append([newx, freq - 1])
                    x = newx
                else:
                    return False
            for i in range(len(usedheap)):
                pusher = usedheap[i]
                heapq.heappush(cnts, pusher)

        return True
                    