---
---

### "Vision is the process of discovering from <br/>images what is present in the world, and where it is."<br/><br/>David Marr<br/>_History of Cognitive Neuroscience_


{% include section.html %}

Based in Lingnan University, our research mainly focuses on ...

{% include section.html %}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

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

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

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
  text=text
%}

{% include section.html %}
### Latest News
{% include newslist.html data="posts" component="post-title" %}
