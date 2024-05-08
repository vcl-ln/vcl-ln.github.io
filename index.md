---
---

<b>The Visual Cognition Lab based at Lingnan University, Hong Kong is led by Prof. Will Hayward. Our current diverse research topics include: person perception (specifically the development of facial familiarity and mechanisms of face recognition), post-COVID19 cognitions and perceptions, and finally, the perceptual and cognitive evaluations of art.</b>

{% include section.html %}

{% capture text %}

Our lab utilizes behavioral tasks alongside EEG and eye-tracking to explore our research topics

{%
  include button.html
  link="projects"
  icon="fa-solid fa-arrow-right"
  text="View our current projects"
  flip=true
  style="text-align:center"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="projects"
  title="Our Current Projects"
  text=text
  flip = true
%}

{% capture text style="text-align:center"%}

The research conducted by the Visual Cognition Lab is diverse, ranging from person perception through to object recognition

{%
  include button.html
  link="publications"
  icon="fa-solid fa-arrow-left"
  text="See our publications"
  flip=true
  style="text-align:center"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="publications"
  title="Our Research"
  text=text
%}

{% capture text %}

Meet the Lab members, both present and past... 

{%
  include button.html
  link="team"
  icon="fa-solid fa-arrow-right"
  text="Meet our team"  
  flip=true
  style="text-align:center"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Our Team"
  flip = true
  text=text
  style="text-align:center"
%}

{% include section.html %}
### Latest News
{% include newslist.html data="posts" component="post-title" %}
