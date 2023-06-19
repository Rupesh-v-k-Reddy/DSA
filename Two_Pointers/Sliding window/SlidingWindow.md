# Sliding Window

> Like two pointers, sliding windows work the same with arrays and strings - the important thing is that
> they're iterables with ordered elements. For the sake of brevity, the first part of this article up until the examples will be focusing on arrays. > However, all the logic is identical for strings.

Sliding window is another common approach to solving problems related to arrays. A sliding window is actually implemented using two pointers! Before we start, we need to talk about the concept of a subarray.

### SubArrays

Given an array, a subarray is a contiguous section of the array. All the elements must be adjacent to each other in the original array and in their original order. For example, with the array [1, 2, 3, 4], the subarrays (grouped by length) are:

```python
[1], [2], [3], [4]
[1, 2], [2, 3], [3, 4]
[1, 2, 3], [2, 3, 4]
[1, 2, 3, 4]
```

A subarray can be defined by two indices, the start and end. For example, with [1, 2, 3, 4], the subarray [2, 3] has a starting index of 1 and an ending index of 2. Let's call the starting index the left bound and the ending index the right bound. Another name for subarray in this context is "window".

---

## When should we use Sliding windows?

There is a very common group of problems involving subarrays that can be solved efficiently with sliding window. Let's talk about how to identify these problems.

**First**, the problem will either explicitly or implicitly define criteria that make a subarray "valid". There are 2 components regarding what makes a subarray valid:

1. A constraint metric. This is some attribute of a subarray. It could be the sum, the number of unique elements, the frequency of a specific element, or any other attribute.
2. A numeric restriction on the constraint metric. This is what the constraint metric should be for a subarray to be considered valid.
   For example, let's say a problem declares a subarray is valid if it has a sum less than or equal to 10. The constraint metric here is the sum of the subarray, and the numeric restriction is <= 10. A subarray is considered valid if its constraint metric conforms to the numeric restriction, i.e. the sum is less than or equal to 10.

**Second**, the problem will ask you to find valid subarrays in some way.

1. The most common task you will see is finding the best valid subarray. The problem will define what makes a subarray better than another. For example, a problem might ask you to find the longest valid subarray.

2. Another common task is finding the number of valid subarrays. We will take a look at this later in the article

> Whenever a problem description talks about subarrays, you should figure out if sliding window is a good option by analyzing the problem description. >If you can find the things mentioned above, then it's a good bet.

## Fixed WIndow Size

In the examples we looked at above, our window size was dynamic. We tried to expand it to the right as much as we could while keeping the window within some constraint and removed elements from the left when the constraint was violated. Sometimes, a problem will specify a fixed length k.

These problems are easy because the difference between any two adjacent windows is only two elements (we add one element on the right and remove one element on the left to maintain the length).

Start by building the first window (from index 0 to k - 1). Once we have a window of size k, if we add an element at index i, we need to remove the element at index i - k. For example, k = 2 and you currently have elements at indices [0, 1]. Now, we add 2: [0, 1, 2]. To keep the window size at k = 2, we need to remove 2 - k = 0: [1, 2].

### Here's some Psuedocode

```python
function fn(arr, k):
    curr = some data to track the window

    // build the first window
    for (int i = 0; i < k; i++)
        Do something with curr or other variables to build first window

    ans = answer variable, probably equal to curr here depending on the problem
    for (int i = k; i < arr.length; i++)
        Add arr[i] to window
        Remove arr[i - k] from window
        Update ans

    return ans
```
