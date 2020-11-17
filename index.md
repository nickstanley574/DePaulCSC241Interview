---
layout: default
title: Home
---

<ul>
  {% for slide in site.slides_test %}
    <li>
      <a href="{{ slide.url }}">{{ slide.title }}</a>
    </li>
  {% endfor %}
</ul>

<ul>
  {% for note in site.notes %}
    <li>
      <a href="{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>