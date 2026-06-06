class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums # create heap array from existing nums
        self.k = k # member k variable
        heapq.heapify(self.minHeap) # heapify nums
        while len(self.minHeap) > self.k: # if initial data stream is larger than size k heappop
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # heap push val into minHeap
        while len(self.minHeap) > self.k: # only if self.minHeap is larger than size k 
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

