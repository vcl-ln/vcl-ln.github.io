---
title: News
nav:
  order: 4
  tooltip: News from the lab
---

## {% include icon.html icon="fa-solid fa-feather-pointed" %}Blog

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}