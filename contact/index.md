---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

## {% include icon.html icon="fa-solid fa-envelope" %}Contact

We are strongly committed to mentoring and supporting the growth of budding researchers. 

If you are interested in joining the lab as a research assistant, PhD student, or MPhil student, feel free to email us. 

We also welcome emails from fellow researchers who would like to collaborate on any of our projects. 

{%
  include figure.html
  image="images/lab/Lingnan.jpg"
  link="https://www.ln.edu.hk/"
  width="400px"
%}

{%
  include button.html
  type="email"
  text=site.links.email
  link=site.links.email
%}

{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://maps.app.goo.gl/2XrocXqvfMWDQfp8A"
%}

{% capture content %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% endcapture %}

{%
  include grid.html
  content=content
  style="square"
%}
