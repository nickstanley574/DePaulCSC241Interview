---
layout: default
---
# Loop Pattern: Iterations with Indexes

```python
# Check whether a list of numbers
# is sorted in increasing order.

lst = [1,2,3,4,5]

for i in lst:
    # now what?
```
{: style="font-size: 1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}

<iframe  align="right" height="550px"  width=790px src="https://repl.it/@nickstanley574/iterationwithindexes?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

{% comment %}
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

{% endcomment %}
