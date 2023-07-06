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

</br>

> Example 2:
> Given the root of a binary tree and an integer targetSum, return true if there exists a path from the root to a leaf such that the sum of the nodes on the path is equal to targetSum, and return false otherwise.

First, what information do we need at each function call? We need the current node, but do we need anything else? If we also keep an integer curr that represents the current sum of the nodes from the root to the current node, we can check this value against targetSum when we find a leaf. Thus, let's have a helper function dfs(node, curr) that returns true if there is a path starting at node and ending at a leaf with a sum equal to targetSum, if we already have curr contributed towards the sum.

What are the base cases? First of all, if we have an empty tree, we can't have a path as there are no nodes, so return false. If we are at a leaf node (which we can check by seeing if both children are null), then return (curr + node.val) == targetSum.

Otherwise, if we are not at a leaf, we could either continue down the left path or the right path. We only need one path to equal targetSum, so return true if either works. Don't forget to add the current node's value to curr.

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False

            # if both children are null, then the node is a leaf
            if node.left == None and node.right == None:
                return (curr + node.val) == targetSum

            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right

        return dfs(root, 0)
```

Again, the time and space complexity are both _O(n)_, where
n is the number of nodes in the tree, as each node is visited at most once and each visit involves constant work. In the worst case scenario for space (straight line), the recursion call stack will grow to the same size as the number of nodes in the tree
<br>

> Example 3: Count Good Nodes in Binary Tree
> Given the root of a binary tree, find the number of nodes that are good. A node is good if the path between the root and the node has no nodes with a greater value.

Again, let's start by thinking about what information we need at each function call (other than the node). At each node, we want to know if the node is good, and to know if the node is good, we need to know the largest value between the root and the node. Let's use an integer maxSoFar to store this.

Then, we can have a function dfs(node, maxSoFar) that returns the number of good nodes in the subtree rooted at node, where the maximum number seen so far is maxSoFar.

What is the base case? If we have an empty tree, then the answer is 0 because there are no nodes, so there are no good nodes.

The total good nodes in a subtree is the number of good nodes in the left subtree + the number of good nodes in the right subtree + 1 if the current node is a good node. If node.val >= maxSoFar, that means the current node is a good node. Then we also need to find how many good nodes are in the left and right subtrees, which we can do by making recursive calls while updating maxSoFar.

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            left = dfs(node.left, max(max_so_far, node.val))
            right = dfs(node.right, max(max_so_far, node.val))
            ans = left + right
            if node.val >= max_so_far:
                ans += 1

            return ans

        return dfs(root, float("-inf"))
```

The time and space complexity are both _O(n)_ for the exact same reasons as the previous examples.
<br>

> Example 4: 100. Same Tree
> Given the roots of two binary trees p and q, check if they are the same tree. Two binary trees are the same tree if they are structurally identical and the nodes have the same values.

This problem really demonstrates the recursive nature of binary trees.

If p and q are the same tree, then the following is true:

p.val = q.val
p.left and q.left are the same tree
p.right and q.right are the same tree
The main idea is that if any two trees are the same, then their subtrees must also be the same. This gives us a recursive definition of the problem. Because the function we are trying to implement is supposed to tell us if two trees are the same, we can use the function itself to answer conditions 2 and 3.

The following condition can be used to check if p and q are the same tree:

p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)

Now, we need base cases so that the recursion eventually terminates. If p and q are both null, then we can return true, because they are technically both the same (empty) tree. If either p or q is null but not the other, we should return false, as they are clearly not the same tree.

A good way to think about base cases is to think about a tree with only one node. Let's say that p and q are both one-node trees with the same value. The first boolean check p.val == q.val passes, so now we check the subtrees. Because the nodes don't have children, then both calls to the left and right subtrees will trigger the base case and return true.

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

Again, the time and space complexity are both _O(n)_ for the same reasons as the other examples.
