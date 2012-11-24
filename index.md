---
layout: default
---

I am a PhD student at EPFL. My advisor is Martin Odersky. I am currently
working on [Dependent Object Types](http://github.com/namin/dot), aka
DOT, a calculus which aims to provide a new type-theoretic foundations
for languages like Scala. I am also involved with embedding
domain-specific languages in Scala.

What's here
-----------

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
