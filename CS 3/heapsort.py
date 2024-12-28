import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def insert(self, value):
        heapq.heappush(self.heap, value)
    
    def extract_min(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None  # Return None if the heap is empty

def heapsort(nums):
    sorted_nums = []
    heap = MinHeap()
    for num in nums:
        heap.insert(num)
    while not heap.is_empty():
        sorted_nums.append(heap.extract_min())
    return sorted_nums

# Example usage
nums = [3, 1, 5, 2, 4]
print("Original array:", nums)

sorted_nums = heapsort(nums)
print("Sorted array:", sorted_nums)
