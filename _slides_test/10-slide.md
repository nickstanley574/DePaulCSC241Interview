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
numLst = [ 2, 4, 3, 7 ] |  accum = 0
n      =   2            |  accum = accum  +  n
                        |  accum =   0    +  2 = 2
n      =      4         |  accum = accum  +  n
                        |  accum =   2    +  4 = 6
n      =         3      |  accum = accum  +  n
                        |  accum =   6    +  3 = 9
n      =            7   |  accum = accum  +  n
                        |  accum =   9    +  7 = 16
accum = 16
```
{: style="font-size: 1.1em; padding-right: 70px; padding-top: 0px; float: right; margin-top: 0"}


```python
numLst = [2, 4, 3, 7]
accum = 0
for n in numLst:
    accum = accum + n
print(accum)

--- output ---
16

```
{: style="font-size: 1.1em; padding-left: 40px;"}

**`sum`** is *incremented* by the value of **`num`**.

