---
---

The Visual Cognition Lab based at Lingnan University, Hong Kong is led by Prof. Will Hayward. The research conducted by the Visual Cognition Lab is diverse, ranging from person perception through to post-COVID cognitions and perceptions. Our lab utilises behavioural tasks alongside EEG and eye-tracking to explore our research topics. 

The Visual Cognition Lab is also part of the [Cognitive Science Group](https://cognitive-science.group/) at the Psychology department at Lingnan University.  

{%
  include button.html
  icon="fa-solid fa-handshake-angle"
  type='link'
  text="Check here to join our team!"
  link="join"
  style="button"
%}

<a href="http://eepurl.com/iTdTeM"><center><b>Click here to subscribe to our latest newsletter!</b></center></a>

{% include section.html %}

{% capture text %}

Our current research projects include: the development of facial familiarity, mechanisms of face recognition, post-COVID19 cognitions and perceptions, and the perceptual and cognitive evaluations of art.  

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
  image="images/front_page/will_csc.JPG"
  link="projects"
  title="Our Current Projects"
  text=text
  flip = true
%}

{% capture text style="text-align:center"%}

The research conducted by the Visual Cognition Lab is diverse, ranging from person perception through to object recognition.

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
  image="images/front_page/will_nian_vss.JPG"
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

{%
  include button.html
  link="join"
  text="Join us"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="text-align:center"
%}

{% endcapture %}

{%
  include feature.html
  image="images/front_page/team.png"
  link="team"
  title="Our Team"
  flip = true
  text=text
  style="text-align:center"
%}

{% include section.html %}
### Latest News
{% include newslist.html data="posts" component="post-title" %}
