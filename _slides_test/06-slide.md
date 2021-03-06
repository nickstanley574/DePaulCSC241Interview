---
layout: default
---
# `for` Loop

<img style="padding-right: 10px; " src="../../for_loop_flowchart.svg" alt="for_loop_flowchart" width="520" align="right" >

A `for` loop is used for iterating over a sequence.

**iterate** - the act of repeating; a repetition.

In programing we call objects that can be iterated over **iterable**.

```python
for <variable> in <sequence>:
    <indented code block>
<non-indented statement>
```
{: style="font-size: 1.1em; padding-left: 40px; padding-top: 1px"}
<br>
<hr>

```python
for i in ['sedan','train','truck','plane']:
    print(i)
print('Done.')
```
{: style="font-size: 1.1em; padding-left: 40px; padding-top: 1px"}

{% comment %}

A for is a control flow statement which allows code to be executed repeatedly. 

Another way of saying that is a `for` loop is used for iterating over a sequence.

**iterate** - the act of repeating; a repetition. If I have a shopping list and I read to you the items in apples, Milk, Chicken I am iterating over the items.

In programing we call objects that can be iterated over **iterable**.

Here we have the stucutre of the `for` loop in the python syntax. 

The `<sequence>` must refer to an object that can be iterated over. We can use a `lists` in the sequence postion b/c a list is a iterable object.

When the for loop is executed  it assigns the values in the `<sequence>` to `<variable>` one by one. Any code in the `<indented code block>` will be executed every time the loop runs until the last item in the `<sequence>` is reached.

Flowchart review

{% endcomment %}

