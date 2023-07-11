# BFS on graph Template

**bfs** : uses a queue to keep track of the nodes to be visited
**get_neighbors** :returns a node's neighbors.In an adjacency list representation, this would be returning the list of neighbors for the node. If the problem is about a matrix, this would be the surrounding valid cells

```python
from collections import deque

def bfs(node):
    queue = deque([root])
    visited = set([root])
    while len(queue):
        node = queue.popleft()
        for neighbour in get_neighbors(node):
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.append(neighbour)
```
