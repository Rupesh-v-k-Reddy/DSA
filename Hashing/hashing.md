# hashing

We know that arrays have O(1) random access. Given an arbitrary index, we can access and update its value in the array in constant time. The main constraint with arrays is that they are a fixed size, and the indices have to be integers. Because hash functions can convert any input into an integer, we can effectively remove the constraint of indices needing to be integers. When a hash function is combined with an array, it creates a hash map, also known as a hash table or dictionary.

With arrays, we map indices to values. With hash maps, we map keys to values, and a key can be almost anything. Typically, the only constraint on a hash map's key is that it has to be immutable (this is language dependent but generally a good rule of thumb). Values can be anything.

A hash map is probably the most important concept in all of algorithm interviewing. It is extremely powerful and allows you to reduce the time complexity of an algorithm by a factor of O(n) for a huge amount of problems. Every major language has a built-in implementation of a hash map. For example, in Python they're called dictionaries and declaring one is as simple as dic = {}

## Comparison with arrays

In terms of time complexity, hash maps blow arrays out of the water. The following operations are all O(1) for a hash map:

1. Add an element and associate it with a value
2. Delete an element if it exists
3. Check if an element exists

A hash map also has many of the same useful properties as an array with the same time complexity:

1. Find length/number of elements
2. Updating values
3. Iterate over elements

# Sets

A set is another data structure that is very similar to a hash table. It uses the same mechanism for hashing keys into integers. The difference between a set and hash table is that sets do not map their keys to anything. Sets are more convenient to use when you only care about checking if elements exist. You can add, remove, and check if an element exists in a set all in O(1).

An important thing to note about sets is that they don't track frequency. If you have a set and add the same element 100 times, the first operation adds it and the next 99 do nothing.

## interface guide

```python

# Declaration: a hash map is declared like any other variable. The syntax is {}

hash_map = {}

# If you want to initialize it with some key value pairs, use the following syntax:

hash_map = {1: 2, 5: 3, 7: 2}

# Checking if a key exists: simply use the `in` keyword

1 in hash_map # True
9 in hash_map # False

# Accessing a value given a key: use square brackets, similar to an array.

hash_map[5] # 3

# Adding or updating a key: use square brackets, similar to an array.
# If the key already exists, the value will be updated
hash_map[5] = 6

# If the key doesn't exist yet, the key value pair will be inserted

hash_map[9] = 15

# Deleting a key: use the del keyword. Key must exist or you will get an error.

del hash_map[9]

# Get size

len(hash_map) # 3

# Get keys: use .keys(). You can iterate over this using a for loop.

keys = hash_map.keys()
for key in keys:
print(key)

# Get values: use .values(). You can iterate over this using a for loop.

values = hash_map.values()
for val in values:
print(val)
```
