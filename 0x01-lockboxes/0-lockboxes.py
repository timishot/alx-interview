#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False
    
    visited = set()
    queue = deque([0])  # Start with the first box (index 0)
    visited.add(0)

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]

        for key in keys:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)