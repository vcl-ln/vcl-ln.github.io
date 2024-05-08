---
title: Team
nav:
  order: 3
  tooltip: About our team
---

## {% include icon.html icon="fa-solid fa-users" %} Research Team

{% include section.html %}
{% include list.html data="members" component="portrait" filters="role: pi, group: " %} 
{% include list.html data="members" component="portrait" filters="role: postdoc, group: " %}
{% include list.html data="members" component="portrait" filters="role: phd, group: " %}
{% include list.html data="members" component="portrait" filters="role: undergrad, group: " %}

{% include section.html dark=true %}

We are strongly committed to mentoring and supporting the growth of budding researchers. 
If you are interested in joining the lab as a research assistant, PhD student, or MPhil student, feel free to email us. 

{%
  include button.html
  icon="fa-solid fa-handshake-angle"
  text="Join the Team"
  link="join"
  style="button"
%}

{% include section.html %}

### Alumni
{% include list.html data="members" component="portrait" filters="role: postdoc, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: phd, group: alum" style="small" %}
{% include list.html data="members" component="portrait" filters="role: undergrad, group: alum" style="small" %}

{% include section.html %}

