# Heaps

A heap is a data structure to implement Priority Queue

Note that a priority queue is an abstract data structure. A heap is one of many ways to implement a priority queue. However, people often use the two terms interchangeably. we will use the term "heap".

A heap is a container that stores elements, and supports the following operations:

- Add an element in $O(logn)$
- Remove the minimum element in $O(logn)$
- Find the minimum element in $*O(1)*$

> 📢 A heap can also find the max elements instead of the min elements. If a heap is configured to find/remove the min element, it's called a min heap. If it's configured to find/remove the max element, it's called a max heap.

The ability to find the max/min element in constant time, while only needing logarithmic time to maintain this ability through changes makes a heap an extremely powerful data structure.

## How is a heap implemented?

Like a hash map, all major programming languages will have support for a heap, so you don't need to implement it yourself. In terms of solving algorithm problems, you only really care about the interface, not how it is implemented. But like with hash maps, it's still good to understand the implementation in case you are asked about it in an interview.

> 📢 For brevity, we'll talk about min heaps in this article, although the logic is the same for max heaps.

There are multiple ways to implement a heap, although the most popular way is called a **binary heap** using an array. In the trees and graphs chapter, we saw that binary trees are typically implemented with a `Node` object.

A binary heap implements a binary tree, but with only an array. The idea is that each element in the array is a node in the tree. The smallest element in the tree is the root, and the following property is maintained at every node: if `A` is the parent of `B`, then `A.val <= B.val`. Notice that this property directly implies that the root is the smallest element.

> 📢 Another constraint is that the tree must be a complete Tree

The parent-child relationships are done using math with the indices. The first element at index `0` is the root, then the elements at indices `1` and `2` are the root's children, the elements at indices `3` and `4` are the children of the element at index `1` and the elements at indices `5` and `6` are the children of the element at index `2`, and so on. If a node is at index `i`, then its children are at indices `2i + 1` and `2i + 2`. When elements are added or removed, operations are done to maintain the aforementioned property of `parent.val <= child.val`. The number of operations needed scales logarithmically with the number of elements in the heap, and the process is known as "bubbling up".

> 📢 An existing array of elements can also be converted into a heap in linear time, although the process is complicated. Luckily, some major programming languages have built-in methods to do this.

In many problems, using a heap can improve an algorithm's time complexity from $O(n^2)$ to $O(n.logn)$ which is a massive improvement (for `n = 1,000,000`, this is `50,000` times faster). A heap is a great option whenever you need to find the maximum or minimum of something repeatedly.

### Interface Guide

```python
# In Python, we will use the heapq module
# Note: heapq only implements min heaps
from heapq import *

# Declaration: heapq does not give you a heap data structure.
# You just use a normal list, and heapq provides you with
# methods that can be used on this list to perform heap operations
heap = []

# Add to heap
heappush(heap, 1)
heappush(heap, 2)
heappush(heap, 3)

# Check minimum element
heap[0] # 1

# Pop minimum element
heappop(heap) # 1

# Get size
len(heap) # 2

# Bonus: convert a list to a heap in linear time
nums = [43, 2, 13, 634, 120]
heapify(nums)

# Now, you can use heappush and heappop on nums
# and nums[0] will always be the minimum element
```
