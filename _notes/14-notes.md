---
layout: default
---
# Loop Pattern: Iterations with Indexes
... consider the problem of checking wheater a list of number is sorted in increasing order. ... You need Indexes interation

```python
#index:  0  1  2  3  4
lst1 = [10,20,40,30,50]
lst2 = [10,20,30,40,50]

def isSorted(lst):
  for i in range(len(lst)):   # range(len(lst)-1)
    print (lst[i], ">", lst[i+1])
    if lst[i] > lst[i+1]:
      print ("False")
      return False
  return True
 ````
Indexing operator: `list[index]`

 We got a out of bounds. The reason why is another off by 1 error. Since we do `i+1` that means on the last iteration. When i is `4` `i+1` is `5` and there is no idea at index 5.

 To fix this we need to doe a -1 at the end of our range().

