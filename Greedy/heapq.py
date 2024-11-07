import heapq

# Initialize a list and transform it into a min-heap
numbers = [5, 3, 8, 1, 2]
heapq.heapify(numbers)

print("Heap:", numbers)  # Output shows numbers arranged in heap order

# Push a new element onto the heap
heapq.heappush(numbers, 0)
print("After heappush:", numbers)

# Pop the smallest element from the heap
while numbers:
    smallest = heapq.heappop(numbers)
    print("Smallest element:", smallest)
    print("Heap after heappop:", numbers)
