# Introduction into `for` Loops

<img style="padding-right: 150px; padding-top:40px" src="../../airplane_loop.png" alt="airplane_loop" width="700" align="right" >

### {{ site.time | date: '%B %d, %Y' }}

### Nicholas Stanley

---------------------------------------------------------------------------------------------------------------------------------

# Hello World

```python
# Yep a good old hello world cliché.
>>> print('Hello, world!')
'Hello, world!'
>>>
>>> import getpass
>>> print(getpass.getuser())
'nick.stanley'
>>>
>>> education()
'DePaul University'
'   * Bachelors in Computer Science             2016'
'   * Masters in Science Software Engineering   2019'
'       * Graduate Assistant Program Tutor      2016 - 2019'
>>>
>>> industry()
'   * Discovery Education       2015 - 2019'
'   * Backstop Solutions Group  2019 - Present'
```

---------------------------------------------------------------------------------------------------------------------------------

# Overview and Goals

* A quick `list` review

* Introduction into the `for` loops.

* Review the `range()` method.

* Explore Loop patterns Counter, Accumulator, index iteration

### Assumptions

* You already have a basic understanding of the Python syntax 🐍. (indentation, `print()`, variable expressions)

* You are aware of what a `list` is and just need a quick refresher.

---------------------------------------------------------------------------------------------------------------------------------

# Quick List Overview

A list in python is just a sequence of objects.

Lists are represented as a comma-separated sequence enclosed with square brackets.

```python

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
```

---------------------------------------------------------------------------------------------------------------------------------

# Quick List Overview

A list's items are indexed starting a `0`.
```python
# index:
#              0       1       2       3
vehicles = ['sedan','train','truck','plane']
```

Indexing operator: `list[index]`.

Lets access `'trains'` which is the 2nd item, but b/c indexing starts at `0` the 2nd item is at index `1`.
```python
>>> vehicles = ['sedan','train','truck','plane']
>>> vehicles[1]
>>> 'train'
```

---------------------------------------------------------------------------------------------------------------------------------

# `for` Loop

<img style="padding-right: 50px; " src="../../for_loop_flowchart.jpg" alt="for_loop_flowchart" width="520" align="right" >

A `for` loop is used for iterating over a sequence.

**iterate** - the act of repeating; a repetition.

In programing we call objects that can be iterated over **iterable**.

```python
for <variable> in <sequence>:
    <indented code block>
<non-indented statement>
```
{: style="font-size: 1.2em; padding-left: 40px; padding-top: 1px"}

---------------------------------------------------------------------------------------------------------------------------------


# `list` in `<sequence>`
<img style="padding-right: 50px; " src="../../for_loop_flowchart.jpg" alt="for_loop_flowchart" width="520" align="right" >

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

---------------------------------------------------------------------------------------------------------------------------------


# Variable in `<sequence>`
<img style="padding-right: 50px; " src="../../for_loop_flowchart.jpg" alt="for_loop_flowchart" width="520" align="right" >
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

---------------------------------------------------------------------------------------------------------------------------------

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

---------------------------------------------------------------------------------------------------------------------------------

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

---------------------------------------------------------------------------------------------------------------------------------

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

---------------------------------------------------------------------------------------------------------------------------------


# End