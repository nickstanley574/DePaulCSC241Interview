---
layout: default
title: Home
---
<ul>
  {% for slide in site.slides %}
    <li>
      <a href="{{ slide.url }}">{{ slide.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>