---
layout: default
---
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

