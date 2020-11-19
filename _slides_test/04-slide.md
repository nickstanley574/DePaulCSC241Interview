---
layout: default
---
# `list` Overview: Indexes

A list's items are indexed starting at `0`.
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
