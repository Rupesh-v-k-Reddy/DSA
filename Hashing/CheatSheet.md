## Hashing

### Count the no of subarrays with exact constraint:

We use “curr” to tracak the prefix sum

At any index i, the sum up to i is curr. If there is an index j whose prefix is curr-k then the sum of subarray with elements from j+1 to i is curr-(curr-k) = k

Because the array can have -ve values , the same prefix can occur multiple times . we use a hashmap “counts” to track how many times a prefix has occured

At every index i the frequency of curr-k is equal to the no of subarrays . Whose sum is equal to K that end at i. Add it to the answer.

```python
# find no of subarrays equal to K:
nums = [1, 2, 1, 2, 1]
k = 3
counts = {}
counts[0] = 1
ans = curr = 0
for i in nums:
    curr += i
    ans += counts[curr-k]
    counts += 1
return ans
```

## Anagrams

The cleanest way to know if 2 strings are anagrams of each other is by checking if they are equal after both being sorted

Also all strings will be the same when sorted .so we can use the sorted version as a key

We can map these keys to the groups themselves in a hashmap and then our answer is just the values of the hashmap

```python
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for s in strings:
    key = "".join(sorted(s))
    groups[key].append(s)
return groups.values()
```

### Hshing indices as values

```python
cards = [3, 4, 2, 3, 4, 7]
dic = defaultdict(list)
for i in range(len(cards)):
    dic[cards[i]].append(i)

#output
{3: [0, 3], 4: [1, 4], 2: [2], 7: [5]}
```

### Get digit sum:

```python

def getdigitsum(n):
    digitsum = 0
    while n:
        digitsum += n % 10
        n // 10
    return digitsum

print(getdigitsum(18)) #1+8 = 9
```

## Counting the no of pairs with exact constraint

```python
n =[1,5,11,5,1,7,11]
k =16
counts = {}
ans = 0
for num in n:
    compliment = k-num
    ans += counts[compliment]
    counts[num] +=1
return ans

#ans = 4 =>[5,11][11,5][5,11],[5,11]
#indices		1 2    2 3  3 6    1 6
```
