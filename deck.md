# Introduction into `for` Loops

<img style="padding-right: 150px; padding-top:40px" src="../../airplane_loop.png" alt="airplane_loop" width="700" align="right" >

### {{ site.time | date: '%B %d, %Y' }}

### Nicholas Stanley

{% comment %}
Play it by ear.
{% endcomment %}

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
'   * Bachelors in Computer Science         2016'
'   * Masters in Software Engineering       2019'
'       * Graduate Assistant Program Tutor  2016 - 2019'
>>>
>>> industry()
'   * Discovery Education       2015 - 2019'
'   * Backstop Solutions Group  2019 - Present'
```
{% comment %}

* I graduated from DePaul University with a Bachelors Degree in Computer Science in 2016

* I also graduated from DePaul with a Master in Software Engineering in 2019

* During my master program I was in the Graduate Assistant program has a Tutor.

* I am currently working at Backstop solutions as a Senior DevOps Engineer leading a team of 4.

{% endcomment %}


---------------------------------------------------------------------------------------------------------------------------------
# Overview and Assumptions

* `list` Review

* `for` Loop Introduction

* `range()`

* Loop Patterns - counter, accumulatorm, index iteration

### Assumptions

* The audience already has a basic understanding of the Python syntax 🐍.
    * indentation
    * `print()`
    * variable expressions: `x = 1 `
    *  Arithmetic operators: `- , + , /  , %`
    * `if else` statements and comparison operators `< , <= , >=, >, == `
<br><br>
* The audience is aware of what a `list` is and just needs a refresher.

{% comment %}

* Let review what we are going to talk about in  presentation.

    * We will to do a quick list review. What they are, and list indexing.

    * Using `list` we are then going to explore what a `for` loop is and now it works.

    * We are going to introuce the built in range() method.

    * And then we are going to explore some loop pattern including counter, accumulator and index iteration.

*  For this talk I made some assumptions

    * One the audience has a basic understanding Python.

        * indentation,   the `print()` statement

        * basic if else statements

        * basic Arithmetic operators and Comparison operators,
{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
# Quick `list` Overview

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

{% comment %}

We humble human need to keep track of multiple things in our daily lives and to do that we make lists, a todo list, shopping list, a book list.

In programming sometime you need to do the same thing and keep track of multiple values.

To accomplish this, Python as a built in type and, because we programmers are unimaginative and like quick and effective communication, it called you guest it a list.

{% endcomment %}


---------------------------------------------------------------------------------------------------------------------------------
# Quick `list` Overview

A list's items are indexed starting a `0`.
```python
# index:       0       1       2       3
vehicles = ['sedan','train','truck','plane']
```

<iframe align="right" height="410px" width="676px" src="https://repl.it/@nickstanley574/counterlloop?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


Indexing operator: `list[index]`.
{: style="font-size: 1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}


Lets access `'trains'` which is the 2nd item, but b/c indexing
<br>
starts at `0` the 2nd item is at index `1`.
{: style="font-size: 1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}


```python
>>> vehicles = ['sedan','train','truck','plane']
>>> vehicles[1]
>>> 'train'
```
{: style="font-size: 1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}




{% comment %}

You can also thing of index has position in a list.

A list's items are indexed starting a zero.

Lists are incredibly powerful objects and have a lot of built in
methods to solve a whole host of problems, but for the
purpose of this talk we are going to skip over them and
focus on `for` loop and use the list to explore `for` list usability.



{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
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

<hr>

```python
for i in ['sedan','train','truck','plane']:
    print(i)
print('Done.')
```
{: style="font-size: 1.1em; padding-left: 40px; padding-top: 1px"}

---------------------------------------------------------------------------------------------------------------------------------
# `for` Loop

<img style="padding-right: 10px; " src="../../for_loop_flowchart.svg" alt="for_loop_flowchart" width="520" align="right" >

```python
for <variable> in <sequence>:
    <indented code block>
<non-indented statement>
```
{: style="font-size: 1.1em; padding-left: 40px;"}

<hr>

<div style="padding-top: 10px;">
    <iframe width="850" height="300" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=for%20i%20in%20%5B'sedan','train','truck','plane'%5D%3A%0A%20%20%20%20print%28i%29%0Aprint%28'Done.'%29&codeDivHeight=410&codeDivWidth=450&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
</div>
{: style="font-size: 1.1em; padding-left: 0px;"}

---------------------------------------------------------------------------------------------------------------------------------
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
    print(i)

--- output ---
0
1
2
3
4
5
```
{: style="font-size: 1.1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}


<iframe align="right" height="420px" width="900px" src="https://repl.it/@nickstanley574/counterlloop?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

---------------------------------------------------------------------------------------------------------------------------------
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

---------------------------------------------------------------------------------------------------------------------------------
# Accumulator Loop

<div style="padding-top: 85px;"></div>

<iframe width="775" height="320" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=numLst%20%3D%20%5B2,%204,%203,%207%5D%0Aaccum%20%3D%200%0Afor%20n%20in%20numLst%3A%0A%20%20%20%20accum%20%3D%20accum%20%2B%20n%0Aprint%28accum%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


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
{: style="font-size: 0.895em; padding-right: 3px; padding-top: 0px; float: right; margin-top: 0"}

---------------------------------------------------------------------------------------------------------------------------------
# Iterations with Indexes

```python

vehicles = ['sedan','train','truck','plane']

# Iterating thought the items
for v in vehicles:
    print(v)
print('Done.')


# Iterating though the indexs
for i in range(len(vehicles)):
    print(vehicles[i])
print('Done.')

```
{: style="font-size: 1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}

<iframe  align="right" height="550px"  width=790px src="https://repl.it/@nickstanley574/iterationwithindexes?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
---------------------------------------------------------------------------------------------------------------------------------
# Iterations with Indexes

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

the car is

{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
# Loop Pattern: Nested Loop




---------------------------------------------------------------------------------------------------------------------------------
# End


---------------------------------------------------------------------------------------------------------------------------------
# Accumulator Loop


```python
# find the index of the third occurrence of a word.

# index    0     1     2     3     4     5
words = ['cat','rug','cat','pie','cat','jet']

```