# Linked List

> Before starting this chapter, you need to have a basic understanding of object-oriented programming concepts, including classes, objects, and >attributes.

Let's start by introducing the concept of a node. A node can be thought of as an element, but with more information than just one piece of data like an integer or string. Nodes are an abstract idea - for example, let's say you had an array <span style="color:red; opacity: 0.80">**[1,2,3]**</span>. You could imagine each element as a node with two pieces of information: the integer, and the index. So the second element would be something like

```
data: 2
index: 1
```

A linked list is a data structure that is similar to an array. It also stores data in an ordered manner, but it is implemented using node objects (you will have a custom class that defines the node object). Each node will have a "next" pointer, which points to the node representing the next element in the sequence.

Here's some example code for creating a linked list to represent the data <span style="color:red; opacity: 0.80">1 --> 2 --> 3</span>. As you can see, the class that defines a node has a field <span style="color:red; opacity: 0.80">val</span> which will hold the data, and a <span style="color:red; opacity: 0.80">next </span>pointer which references the next node. In the code, we are creating three nodes, one for each number, then setting the <span style="color:red; opacity: 0.80">next </span> pointers accordingly

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.next = three
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)
```

We call the node with the <span style="color:red; opacity: 0.80">**1**</span> the <span style="color:red; opacity: 0.80">**head**</span> because it is the start of the linked list. Usually, you will want to keep a reference to the head. This is because the head is the only node from where you can reach all elements in the linked list (you might have noticed that we can't go backward), so by keeping a reference to it, you ensure that you never "lose" any elements

## Mechanics of Linked Lists

### Assignment

```python
ptr = head
head = head.next
head = None
```

After these lines of code, <span style="color:red; opacity: 0.80">**ptr**</span> still refers to the original <span style="color:red; opacity: 0.80">**head**</span> node, even though the <span style="color:red; opacity: 0.80">**head**</span> variable changed. This is the first important concept: variables remain at nodes unless they are modified directly (<span style="color:red; opacity: 0.80">**ptr = something**</span> is the only way to modify ptr).

### chaining .next

If you have multiple <span style="color:red; opacity: 0.80">**.next**</span>, for example <span style="color:red; opacity: 0.80">**head.next.next**</span>, everything before the final <span style="color:red; opacity: 0.80">**.next**</span> refers to one node. For example, given a linked list <span style="color:red; opacity: 0.80">**1 -> 2 -> 3**</span>, if you have <span style="color:red; opacity: 0.80">**head**</span> pointing at the first node, and you do <span style="color:red; opacity: 0.80">**head.next.next**</span>, you are actually referring to <span style="color:red; opacity: 0.80">**2.next**</span>, because <span style="color:red; opacity: 0.80">**head.next**</span> is the <span style="color:red; opacity: 0.80">**2**</span>. We'll soon see that this is a very useful technique.

### Traversal

Iterating forward through a linked list can be done with a simple loop. This is the usual code that you will use to do so: as an example let's get the sum of all values from an integer linked list:

```python
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next

    return ans
```

> The final node's <span style="color:red; opacity: 0.80">**next**</span> pointer is <span style="color:red; opacity: 0.80">**null**</span>. Therefore, after doing <span style="color:red; opacity: 0.80">**head = head.next**</span> at the final node, <span style="color:red; opacity: 0.80">**head**</span> becomes <span style="color:red; opacity: 0.80">**null**</span> and the while loop ends.

Moving to <span style="color:red; opacity: 0.80">**head.next**</span> is the equivalent of iterating to the next element in an array. Traversal can also be done recursively:

```python
def get_sum(head):
    if not head:
        return 0

    return head.val + get_sum(head.next)
```

## Types of Linked Lists

### Singly Linked Lists

This is the most common type of linked list and the one that is given in the code above. In a singly linked list, each node only has a pointer to the next node. This means you can only move forward in the list when iterating. The pointer used to reference the next node is usually called <span style="color:red; opacity: 0.80">**next**</span>

Let's say you want to add an element to a linked list so that it becomes the element at position <span style="color:red; opacity: 0.80">**i**</span>. To do this, you need to have a pointer to the element currently at position <span style="color:red; opacity: 0.80">**i-1**</span>. The next element (currently at position <span style="color:red; opacity: 0.80">**i**</span>), call it <span style="color:red; opacity: 0.80">**x**</span>, will be pushed to the element at position <span style="color:red; opacity: 0.80">**i+1**</span> after the insertion. This means that <span style="color:red; opacity: 0.80">**x**</span> should become the <span style="color:red; opacity: 0.80">**next**</span> node to the one being added, and the node being added should become the <span style="color:red; opacity: 0.80">**next**</span>next node to the one currently at <span style="color:red; opacity: 0.80">**i - 1**</span>. Here's some code demonstrating:

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add
```

Let's say you want to delete the element at position i. Again, you need to have a pointer to the element currently at position i - 1. The element at position i + 1, call it x, will be shifted over to be at position i after the deletion. Therefore, you should set x as the next node to the element currently at position i - 1. Here's some code demonstrating:

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next
```

As mentioned before, when you have a reference to the node at i - 1, then insertion and deletion is O(1). However, without that reference, you need to obtain the reference by iterating from the head, which for an arbitrary position is O(n).

### Doubly linked list

A doubly linked list is like a singly linked list, but each node also contains a pointer to the previous node. This pointer is usually called prev, and it allows iteration in both directions.

n a singly linked list, we needed a reference to the node at i - 1 if we wanted to add or remove at i. This is because we needed to perform operations on the prevNode. With a doubly linked list, we only need a reference to the node at i. This is because we can simply reference the prev pointer of that node to get the node at i - 1, and then do the exact same operations as above.

With a doubly linked list, we need to do extra work to make also update the prev pointers.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
```
