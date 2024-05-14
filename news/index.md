---
title: News
nav:
  order: 4
  tooltip: News from the lab
---

## {% include icon.html icon="fa-solid fa-feather-pointed" %}News

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}

{% include list.html data="news" component="post-excerpt" %}