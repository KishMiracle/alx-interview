#!/usr/bin/python3
def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    visited = [False] * n
    
    def dfs(box):
        visited[box] = True
        for key in boxes[box]:
            if not visited[key]:
                dfs(key)

    dfs(0)
    return all(visited)
