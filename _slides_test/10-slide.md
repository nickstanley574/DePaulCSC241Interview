---
layout: default
---
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

