## DFS:

```python
def dfs(node):
    if node == None:
        return

    dfs(node.left)
    dfs(node.right)
    return
```

### Max depth of Tree

```python
left = dfs(root.left)
right = dfs(root.right)
return max(left,right)+1
# 1 indicates the current level(if we go to the root node we need to
#                               return 1 indicating the current level)
```

### Diameter Formula

```python
def maxDiameter(root):
    diameter = 0
    def finddia(root):
        if not root:
            return 0
        nonlocal diameter
        left = finddia(root.left)
        right = finddia(root.right)
        diameter = max(diameter, left+right)
        return max(left, right)+1
    finddia(root)
    return diameter

```

<aside>
📢 The name of each traversal is describing when the current node's logic is performed.

Pre -> before children

In -> in the middle of children

Post -> after children

</aside>

### SameTree:

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right
```

## BFS

```python
from collections import deque

def print_all_nodes(root):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        # do some logic here for the current level

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            # do some logic here on the current node
            print(node.val)

            # put the next level onto the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

### right side view

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            current_length = len(queue)
            ans.append(queue[-1].val) # this is the rightmost node for the current level

            for _ in range(current_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans
```

or

```python
def rightSideView(root):
    q = deque([root])
    ans = []
    while q:
        val = []
        for _ in range(len(q)):
            cur = q.popleft()
            val.append(cur.value)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        ans.append(val[-1])  #if we append just val (ans.append(val)) we get level order traversal
    return ans
#level order traversal = [[3],[9,20],[15,7]]
```

## BST

For each node, all values in its left subtree are less than the value in the node, and all values in its right subtree are greater than the value in the node.

<aside>
📢 Trivia to know: an inorder DFS traversal prioritizing left before right on a BST will handle the nodes in sorted order.

</aside>

```python
# min absolute diff val trick
for i in range(1,len(ans)):
            val = min(val,ans[i]-ans[i-1])
```

### Insert into BST:

```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root :
            return TreeNode(val)
        if(val>root.val):
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root
```
