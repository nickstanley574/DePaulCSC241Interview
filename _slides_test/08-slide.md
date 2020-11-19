---
layout: default
---
# Variable in `<sequence>`

<img style="padding-right: 10px; " src="../../for_loop_flowchart.svg" alt="for_loop_flowchart" width="520" align="right" >
```python
for <variable> in <sequence>:
    <indented code block>
<non-indented statement>
```
{: style="font-size: 1.1em; padding-left: 40px;"}

<hr>

```python
vehicles = ['sedan','train','truck','plane']
for i in vehicles:
    print(i)
print('Done.')

--- output ---
sedan
train
truck
plane
Done.
```
{: style="font-size: 1.1em; padding-left: 40px;"}

{% comment %}

In the pervious example we saw a list hardcoded in the `<sequence>` position of the for loop.

That is not a rule of for loops, in fact is not even the norm.

Ussually we put a variable or method into the `<sequence>` position that refers to or returns a iterable.

Here we can see the same loop has before but instead of having the list hardcoded were are using the `vehicles` variable

{% endcomment %}

