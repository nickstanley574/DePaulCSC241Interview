---
layout: default
---
# Loop Pattern: Nested Loops

A nested loop is a loop within a loop, an inner loop within the body of an outer one. 

```python
for i in range(3):
    print("outer Loop  i=" + str(i))
    for j in range(3):
        print ("   inner loop: i=" + str(i) + " j=" + str(j))

--- output ---
outer Loop  i=0
   inner loop: i=0 j=0
   inner loop: i=0 j=1
   inner loop: i=0 j=2
outer Loop  i=1
   inner loop: i=1 j=0
   inner loop: i=1 j=1
   inner loop: i=1 j=2
outer Loop  i=2
   inner loop: i=2 j=0
   inner loop: i=2 j=1
   inner loop: i=2 j=2
```

{% comment %}
The last loop pattern I am going to introduce in the nested loop.

A nested loop is a loop within a loop, an inner loop within the body of an outer one. 

How this works is that the first pass of the outer loop triggers the inner loop, which executes of the inter loop is done. Then the second pass of the outer loop triggers the inner loop again. This repeats until the outer loop finishes.

With that I am open the floor to question
{% endcomment %}

