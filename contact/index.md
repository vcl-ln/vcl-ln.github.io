---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

## {% include icon.html icon="fa-solid fa-envelope" %}Contact

Our lab is part of the

{%
  include figure.html
  image="images/photo.jpg"
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
