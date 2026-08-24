class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = collections.defaultdict(int)
        for n in hand:
            count[n] += 1
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if not count[i]:
                    return False
                count[i] -= 1
                if not count[i]:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
                    
        return True