---
layout: default
---
# Loop Pattern: Accumulator Loop

A common pattern in loops is to accumulate a value during the iteration of the loop.

<style>
pre {
        margin-top: 0em;
}
</style>

```python
numLst = [ 2, 4, 3, 7 ] |  val = 0
                        |  val = val  +  n
                        |
n      =   2            |  val =  0   +  2 = 2
                        |
n      =      4         |  val =  2   +  4 = 6
                        |
n      =         3      |  val =  6   +  3 = 9
                        |
n      =            7   |  val =  9   +  7 = 16
                        |
val = 16
```
{: style="font-size: 1.1em; padding-right: 70px; padding-top: 0px; float: right; margin-top: 0"}


```python
numLst = [2, 4, 3, 7]
val = 0
for n in numLst:
    val = val + n
print(val)

--- output ---
16

```
{: style="font-size: 1.25em; padding-left: 50px;"}

**`val`** is *incremented* by the value of **`num`**.

{% comment %}

The next for loop pattern we are going to explore is the accumulator loop.

This `for` loop “pattern” used to traverse a sequence, accumulating a value as we go, such as the sum-so-far 

The accumulation pattern includes:
* initializing an “accumulator” variable to an initial value.
* iterating thought the items in a sequence.
* updating the accumulator variable on each iteration.

Ours
* So in our case we we initialize our accumulator variable val.
* When the iterate over the items in numLst.
* Duing each iteration we update val.

{% endcomment %}

