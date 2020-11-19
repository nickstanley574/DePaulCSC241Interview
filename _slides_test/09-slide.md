---
layout: default
---
#  The `range()` Method

`range()` allows users to generate a object of numbers within a given range.

We can put `range()` in the `<sequence>` section of a `for` because it returns a iterable object.

```python
# create a sequence of 6 integers, and print each item in the sequence:
for i in range(6):
    print(i)

--- output ---
0
1
2
3
4
5
```
{: style="font-size: 1.1em; padding-left: 40px;"}

{% comment %}

One of the built in methods that is used a lot with for loop in python in the `range()` method.

READ SLIDE

Similar to list indexing the range method starts at 0. If we say giving me `range(6)` it will give back 0,1,2,3,4,5. Notice there are 6 elements returned, and we start at `0` and end at `5`.

Again this is like list indexing at that is not accident. So keep that in mind.

{% endcomment %}

