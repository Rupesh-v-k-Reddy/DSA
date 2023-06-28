> Example 1: Maximum Depth of Binary Tree.
> Given the root of a binary tree, find the length of the longest path from the root to a leaf.

Let's start with a recursive approach. When thinking about designing recursive functions, a good starting point is always the base case. What is the depth of an empty tree (zero nodes, root is null)? The depth is 0.

> Note: earlier, we said that the depth of the root is 0. This is the usual definition, but in this specific LeetCode problem, the depth for the root is defined as 1 (it's asking for how many nodes are on the path from the root to a leaf), and we need to include the root on this path, hence why we start at 1.

Next, we should think about the relationship between the current node and its children. The problem states that we are looking for a path from the root to a leaf, which means that at the current node, we can only consider either the left or right subtree, not both. If maxDepth(node.left) represents the maximum depth of the left subtree and maxDepth(node.right) represents the maximum depth of the right subtree, then we should take the greater value and add 1 to it (because the current node contributes 1 to the depth).

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
```

It's that simple! Thinking recursively takes some time to get the hang of, but hopefully with the examples in this article, you will gain the intuition needed to quickly solve binary tree problems.
The time and space complexity of tree questions is usually straightforward. The time complexity is almost always
_O(n)_, where
n is the total number of nodes, because each node is only visited once, and at each node, _O(1)_ work is done. If more than _O(1)_ work is done at each node, let's say _O(k)_ work, then the time complexity will be _O(n⋅k)_.

For space complexity, even if you are using recursion, the calls are still placed on the call stack which counts as extra space. The largest the stack will be (for either iterative or recursive) at any time will depend on the tree. For recursion, in the worst case it is _O(n)_ if the tree is just a straight line, so usually, the correct answer to give for space complexity is _O(n)_. If the tree is "complete" (all nodes have 0 or 2 children and each level except the last is full), then the space complexity is _O(logn)_, but this is a best case scenario.
