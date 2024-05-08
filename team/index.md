---
title: Team
nav:
  order: 3
  tooltip: About our team
---

## {% include icon.html icon="fa-solid fa-microscope" %} Leader 
{% capture floatcontent %}
{% include list.html data="members" component="portrait-image" filters="role: pi" %} 
{% endcapture %}

{% include float.html content=floatcontent %}
{% assign member = site.members | where: "slug", "will-hayward" | first %}
{% for position in member.position %}
{% endfor %}

{% include section.html %}
### {% include icon.html icon="fa-solid fa-users" %} Research Team
{% include list.html data="members" component="portrait" filters="role: postdoc, group: " %}
{% include list.html data="members" component="portrait" filters="role: phd, group: " %}
{% include list.html data="members" component="portrait" filters="role: undergrad, group: " %}

{% include section.html dark=true %}

We work with a wide range of outstanding groups from around the world, and we're always on the lookout for new and unique perspectives.
We want to push the frontier of data science and train the next generation of data scientists.

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

