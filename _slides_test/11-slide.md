---
layout: default
---
# Accumulator Loop

<iframe width="780" height="320" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=numLst%20%3D%20%5B2,%204,%203,%207%5D%0Asum%20%3D%200%0Afor%20n%20in%20numLst%3A%0A%20%20%20%20sum%20%3D%20sum%20%2B%20n%0Aprint%28sum%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


<style>
pre {
        margin-top: 0em;
}
</style>

```python
numLst = [ 2, 4, 3, 7 ]     |    sum = 0
n      =   2                |    sum = sum + n
                            |    sum =  0  + 2 = 2
n      =      4             |    sum = sum + n
                            |    sum =  2  + 4 = 6
n      =         3          |    sum = sum + n
                            |    sum =  6  + 3 = 9
n      =            7       |    sum = sum + n
                            |    sum =  9  + 7 = 16
sum = 16
```
{: style="font-size: 0.895em; padding-right: 0px; padding-top: 0px; float: right; margin-top: 0"}

