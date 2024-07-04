from collections import deque

start, end = map(int, input().split())

def BFS(start, end):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, depth = queue.popleft()
        

        if current == end:
            return depth
        

        next_pos = current + 1
        if next_pos <= end and next_pos not in visited:
            visited.add(next_pos)
            queue.append((next_pos, depth + 1))
        
        next_pos = current * 2
        if next_pos <=  end and next_pos not in visited:
            visited.add(next_pos)
            queue.append((next_pos, depth + 1))
    
    return -1

min_depth = BFS(start, end)
print(min_depth)
