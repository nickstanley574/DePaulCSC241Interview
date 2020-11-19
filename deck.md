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
>>> print('Hello, world!!!')
'Hello, world!!!'
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

* I earned a Bachelors Degree in Computer Science from DePaul University in 2016

* I coninuted my education and graduated from DePaul with a Master in Software Engineering in 2019

* During my master program I was in the Graduate Assistant program has a Tutor.

* I worked at a company called Discovery Education which was owned by Discovery Channel and made online cleaning tools for students k-12.

* I am currently working at Backstop solutions as a Senior DevOps Engineer.

{% endcomment %}


---------------------------------------------------------------------------------------------------------------------------------
# Overview and Assumptions

<img style="padding-right: 120px" src="../../perkovic.jpg" alt="book" width="270" align="right" >

* `list` Review

* `for` Loop Introduction

* `range()`

* Loop Patterns - counter, Accumulator, index iteration

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

* Let review what we are going to talk about today.

    * We will to do a quick list review. What they are and list indexing.

    * Using `lists` we are then going to explore what a `for` loop is and how it works.

    * We are going to introuce the built in range() method.

    * And then we are going to explore some loop pattern including counter, accumulator and index iteration.

*  For this talk I made some assumptions
    * One the audience has a basic understanding Python.
        * indentation, the `print()` statement, basic if else statements
        * basic Arithmetic operators and Comparison operators
        * You can think of this has a week 3-4 topic.

I used the "Introduction to Computering Using Python" by Prof. Perkovic to help develop this talk. 

With that lets get started with our list overview.
{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
# `list` Overview: Structure

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

To accomplish this, Python as a built in type and, because we programmers are unimaginative , it called you guest it a list.

Talk about slide.
{% endcomment %}


---------------------------------------------------------------------------------------------------------------------------------
# `list` Overview: Indexes

A list's items are indexed starting a `0`.
```python
# index:       0       1       2       3
vehicles = ['sedan','train','truck','plane']
```

<iframe align="right" height="410px" width="676px" src="https://repl.it/@nickstanley574/counterlloop?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


Indexing operator: `list[index]`.
{: style="font-size: 1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}


Lets access `'train'` which is the 2nd item, but b/c indexing
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

You can think of index has position in a list.

A list's items are indexed starting a zero. This pattern you will see thoughout your programing life. 

Indexing operator is a list bracket the index you want closed bracket.

Lets explore this. If the embeded IDE is to small please let me know. 

OUT OF BOUNDS EXAMPLE: vehicles[4]


{% endcomment %}
---------------------------------------------------------------------------------------------------------------------------------
# `list` Overview: `len()`

The `len()` function returns the number of items in a list.

```python
>>> vehicles = ['sedan','train','truck','plane']
>>> len(vehicles)
>>> 4
>>>
>>> nums = [1,3,4,2,7,2]
>>> len(nums)
>>> 6
```

{% comment %}

SLIDE

len is a function buit into python that returns the number if items the list.

Lists are incredibly powerful objects and have a lot of built in methods to solve a whole host of problems, but for the purpose of this talk we are going to move foward to the `for` loop and use lists to explore `for` usability.
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

{% comment %}

Lets explore this loop one more time interativly.

I am using a tool called PYTHON VISUALIZE CODE EXECUTION from pythontutor.com

for this. The RED arrow is the next line to be execute at the green is the line just execute.

{% endcomment %}

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

{% comment %}

In the pervious example we saw a list hardcoded in the `<sequence>` position of the for loop.

That is not a rule of for loops, in fact is not even the norm.

Ussually we put a variable or method into the <sequence> position that refers to or returns a iterable.

Here we can see the same loop has before but instead of having the list hardcoded were are using the `vehicles` variable

{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
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

Similar to list indexing the range method starts at 0. If we say giving me `range(6)` it will give back 0,1,2,3,4,5. Notice there are 6 elements returned, and we start at `0` and end at `5`.

Again this is like list indexing at that is not accident. So keep that in mind.

{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
# Loop Pattern: Counter Loop

We use the counter pattern when we need to execute a block of code for every integer is some range.

The previous `range()` example was a simple counter loop.

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
{: style="font-size: 1.1em; padding-left: 40px; padding-top: 0px; float: left; margin-top: 0"}


<iframe align="right" height="420px" width="900px" src="https://repl.it/@nickstanley574/counterlloop?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

{% comment %}

Read and talk about slide.

Lets explore something a little more intresting. So fair we have seen example that has only printed each item, but we are not limited to print.

We can add other control flow statements, such as if statements.

Lets modify this loop to only print the even numbers.

modulo operator (%), which returns the remainder of dividing two numbers.

Even numbers divided by 2 never have a remainder while odd number always have a remainder.

```python
for i in range(6):
  if (i % 2 == 0):
    print(i)
```

{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
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

**`val`** is *incremented* by **`num`**.

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

---------------------------------------------------------------------------------------------------------------------------------
# Loop Pattern: Accumulator Loop

<div style="padding-top: 85px;"></div>

<iframe width="775" height="320" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=numLst%20%3D%20%5B2,%204,%203,%207%5D%0Aval%20%3D%200%0Afor%20n%20in%20numLst%3A%0A%20%20%20%20val%20%3D%20val%20%2B%20n%0Aprint%28val%29%0A&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


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
{: style="font-size: 0.9em; padding-right: 5px; padding-top: 0px; float: right; margin-top: 0"}

{% comment %}
Lets explore this loop one more time interativly.
{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
# Loop Pattern: Iterations thoughout the Indexes

```python

vehicles = ['sedan','train','truck','plane']

# Iterating thought the items
for v in vehicles:
    print(v)
print('Done.')


# Iterating though the indexes
for i in range(len(vehicles)):
    print(vehicles[i])
print('Done.')

```
{: style="font-size: 1em; padding-right: 0px; padding-top: 0px; float: left; margin-top: 0"}

<iframe  align="right" height="550px"  width=790px src="https://repl.it/@nickstanley574/iterationwithindexes?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

{% comment %}

In every example we have Iterating thought the items of a list, python is very nice to use that is know how to iterate over the items, but there is another way.

We can iterating though the indexs. Remeber the `range()` and `len()` methods we talked about eailer? We can use those to iterate over a list though the indexes.

REPT.IT DEMO

Indexing operator: list[index]

The index iteration is more complicate and less intuitive than the iterate though the items approach so why use it? 

There are situations when you need to iterate by the index, for eaxmple ... 

{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
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
... consider the problem of checking weather a list of number is sorted in increasing order.

You need Indexes interation

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
---------------------------------------------------------------------------------------------------------------------------------
# Loop Pattern: Nested Loops

A nested loop is a loop within a loop, an inner loop within the body of an outer one. 

```python
for i in range(3):
    print("Outer Loop  i=" + str(i))
    for j in range(3):
        print ("inner loop: i=" + str(i) + " j=" + str(j))

--- output ---
Outer Loop  i=0
inner loop: i=0 j=0
inner loop: i=0 j=1
inner loop: i=0 j=2
Outer Loop  i=1
inner loop: i=1 j=0
inner loop: i=1 j=1
inner loop: i=1 j=2
Outer Loop  i=2
inner loop: i=2 j=0
inner loop: i=2 j=1
inner loop: i=2 j=2

```



{% comment %}
The last loop pattern I am going to introduce in the nested loop.

A nested loop is a loop within a loop, an inner loop within the body of an outer one. 

How this works is that the first pass of the outer loop triggers the inner loop, which executes to completion. Then the second pass of the outer loop triggers the inner loop again. This repeats until the outer loop finishes.
{% endcomment %}

---------------------------------------------------------------------------------------------------------------------------------
# Questions

<img style="padding-right: 200px; padding-top:20px" src="../../question-mark.jpg" alt="question" width="700" align="right" >



---------------------------------------------------------------------------------------------------------------------------------

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.content {
    height: 85%;
    padding-left: 0px;
}
</style>

<img style="padding-top:70px" src="../../thankyou.jpg" alt="thankyou" width="900" >
