---
---

### "Vision is the process of discovering from <br/>images what is present in the world, and where it is."<br/><br/>David Marr<br/>_History of Cognitive Neuroscience_


{% include section.html %}

Based in Lingnan University, our research mainly focuses on ...

{% include section.html %}

{% capture text %}

We conduct research with ...

{%
  include button.html
  link="research"
  icon="fa-solid fa-arrow-left"
  text="See our publications"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

We are strongly committed to mentoring young scientists

{%
  include button.html
  link="team"
  icon="fa-solid fa-arrow-right"
  text="Meet our team"  
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Our Team"
  flip = true
  text=text
%}

{% include section.html %}
### Latest News
{% include newslist.html data="posts" component="post-title" %}
