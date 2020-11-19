---
layout: default
---
# Loop Pattern: Iterations thoughout the Indexes

```python

vehicles = ['sedan','train','truck','plane']

# Iterating through the items
for v in vehicles:
    print(v)
print('Done.')


# Iterating through the indexes
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

