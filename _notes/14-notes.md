---
layout: default
---
# Loop Pattern: Iterations with Indexes

```python
lst1 = [1,2,3,4,5]
lst2 = [1,2,4,3,5]

def isSorted(lst):
  for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
      return False
  return True
 ````   
