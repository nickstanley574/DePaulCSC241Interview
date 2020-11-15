---
layout: default
---

# Accumulator Loop

A common pattern in loops is to accumulate a value during the iteration of the loop.

<style>
pre {
        margin-top: 0em;
}
</style>

```python
numLst = [ 2, 4, 3, 7 ]     |    sum = 0
n      =   2                |    sum = sum + n
                            |    sum =  0  + 2 = 2
n      =      4             |    sum = sum + n
                            |    sum =  2  + 4 = 6
n      =         3          |    sum = sum + n
                            |    sum =  6  + 3 = 9
n      =            7       |    sum = sum + n
                            |    sum =  9  + 7 = 16
sum = 16
```
{: style="font-size: 1.1em; padding-right: 70px; padding-top: 0px; float: right; margin-top: 0"}


```python
numLst = [2, 4, 3, 7]
sum = 0
for n in numLst:
    sum = sum + n
print(sum)

--- output ---
16

```
{: style="font-size: 1.1em; padding-left: 40px;"}

**`sum`** is *incremented* by the value of **`num`**.

