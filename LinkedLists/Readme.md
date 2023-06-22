# Linked List

> Before starting this chapter, you need to have a basic understanding of object-oriented programming concepts, including classes, objects, and >attributes.

Let's start by introducing the concept of a node. A node can be thought of as an element, but with more information than just one piece of data like an integer or string. Nodes are an abstract idea - for example, let's say you had an array [1, 2, 3]. You could imagine each element as a node with two pieces of information: the integer, and the index. So the second element would be something like

data: 2
index: 1

A linked list is a data structure that is similar to an array. It also stores data in an ordered manner, but it is implemented using node objects (you will have a custom class that defines the node object). Each node will have a "next" pointer, which points to the node representing the next element in the sequence.

Here's some example code for creating a linked list to represent the data 1 --> 2 --> 3. As you can see, the class that defines a node has a field val which will hold the data, and a next pointer which references the next node. In the code, we are creating three nodes, one for each number, then setting the next pointers accordingly

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

We call the node with the 1 the **head** because it is the start of the linked list. Usually, you will want to keep a reference to the head. This is because the head is the only node from where you can reach all elements in the linked list (you might have noticed that we can't go backward), so by keeping a reference to it, you ensure that you never "lose" any elements

## Mechanics of Linked Lists

### Assignment

```python
ptr = head
head = head.next
head = None
```

### chaining .next

If you have multiple **.next**, for example **head.next.next**, everything before the final **.next** refers to one node. For example, given a linked list **1 -> 2 -> 3**, if you have **head** pointing at the first node, and you do **head.next.next**, you are actually referring to **2.next**, because **head.next** is the **2**. We'll soon see that this is a very useful technique.

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

> The final node's **next** pointer is **null**. Therefore, after doing **head = head.next** at the final node, **head** becomes **null** and the while loop ends.

Moving to **head.next** is the equivalent of iterating to the next element in an array. Traversal can also be done recursively:

```python
def get_sum(head):
    if not head:
        return 0

    return head.val + get_sum(head.next)
```
