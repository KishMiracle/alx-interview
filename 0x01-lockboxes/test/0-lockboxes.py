from collections import deque

def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]
        
        for key in keys:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
