Example 1:Binary Tree Right Side View

> Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.

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

This algorithm has a time and space complexity of
_O(n)_ for the same reasons as the algorithms in the previous article. We visit each node only once and perform a constant amount of work at each node. The queue could hold up to _O(n)_ nodes.

---

Example 2 : Find Largest Value in Each Tree Row

> Given the root of a binary tree, return an array of the largest value in each row of the tree.

In the context of a binary tree, row and level mean the same thing. Again, each iteration inside the while loop represents going through a level. Therefore, we can just use an integer currMax to find the largest value at each level. Notice how similar the code is between this example and the previous example.

```python
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            current_length = len(queue)
            curr_max = float("-inf") # this will store the largest value for the current level

            for _ in range(current_length):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(curr_max)

        return ans
```

The time and space complexity is _O(n)_ for the same reasons as the previous example.
