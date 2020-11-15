# Introduction into `for` Loops

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
