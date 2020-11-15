---
layout: default
---

# Quick List Overview

A list's items are indexed starting a zero. You can also thing of index has position. Like get me the item at position 2.
{% highlight python %}
# index       0       1       2       3
vehicles = ['sedan','train','truck','plane']
{% endhighlight %}

To access individual items in the list we can use the indexing operator `list[index]`.

Lets access `'trains'` which is the 2nd item, but b/c indexing starts at 0 the 2nd item is at position 1.
{% highlight python %}
>>> vehicles = ['sedan','train','truck','plane']
>>> vehicles[1]
>>> 'train'
{% endhighlight %}
