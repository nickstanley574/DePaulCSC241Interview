# Introduction into `for` Loops

<img style="padding-right: 150px; padding-top:40px" src="../../airplane_loop.png" alt="airplane_loop" width="700" align="right" >

### {{ site.time | date: '%B %d, %Y' }}

### Nicholas Stanley



---

# Hello World

{% highlight python %}
# Yep good old hello world cliché.
print('Hello, world!')
{% endhighlight %}


---

# Overview and Goals

* A quick `list` review

* Introduction into the For Loop

* Review the `range()` method.

* Explore Loop patterns Counter, Accumulator, index iteration

### Assumptions

* You already have a basic understanding of the Python syntax 🐍. (indentation, `print()`, variable expressions)

* You are aware of what a list is and just need a quick refresher.

---

# Quick List Overview

A list in python is just a sequence of objects.

Lists are represented as a comma-separated sequence enclosed with square brackets.

{% highlight python %}
#          +----------------------------------- start of list with open square bracket [
#          |
#          |   +------------------------------- item in a list can be any type they are strings
#          |   |
#          |   |   +--------------------------- comma-separates items ,
#          |   |   |
#          |   |   |                       +--- end of list with closed square bracket ]
#          |   |   |                       |
#          ▼   ▼   ▼                       ▼
vehicles = ['sedan','train','truck','plane']
{% endhighlight %}

---

# Quick List Overview

A list's items are indexed starting a `0`.
{% highlight python %}
# index:
#              0       1       2       3
vehicles = ['sedan','train','truck','plane']
{% endhighlight %}


Indexing operator: `list[index]`.

Lets access `'trains'` which is the 2nd item, but b/c indexing starts at `0` the 2nd item is at index `1`.
{% highlight python %}
>>> vehicles = ['sedan','train','truck','plane']
>>> vehicles[1]
>>> 'train'
{% endhighlight %}

---

# `for` Loop

<img style="padding-right: 50px; " src="../../for_loop_flowchart.jpg" alt="for_loop_flowchart" width="475" align="right" >


A `for` loop is used for iterating over a sequence.

**iterate** - the act of repeating; a repetition.

In programing we call objects that can be iterated over **iterable**.


```python
for <variable> in <sequence>:
    <indented code block>
<non-indented statement>
```
{: style="font-size: 1.2em; padding-left: 40px; padding-top: 1px"}




---

# `list` in `<sequence>`
<img style="padding-right: 50px; " src="../../for_loop_flowchart.jpg" alt="for_loop_flowchart" width="475" align="right" >

```python
for <variable> in <sequence>:
    <indented code block>
<non-indented statement>
```
{: style="font-size: 1.1em; padding-left: 40px;"}

<hr>

```python
for i in ['sedan','train','truck','plane']:
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
---

# Variable in `<sequence>`

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
```
{: style="font-size: 1.1em; padding-left: 40px; padding-top: 1px"}

---
#  The `range()` Function

`range()` allows users to generate a object of numbers within a given range.

We can put `range()` in the `<sequence>` section of a `for` b/c it returns a iterable object.

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

---

# Counter Loop

We use the counter pattern when we need to execute a block of code for every integer is some range. 

The pervious `range()` example was a simple counter loop.

```python
for i in range(6):
    if (i % 2) == 0:
        print(i)

--- output ---
0
2
4
```
{: style="font-size: 1.1em; padding-left: 40px;"}

