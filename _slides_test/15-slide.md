---
layout: default
---
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

