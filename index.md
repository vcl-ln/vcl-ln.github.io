---
---

The Visual Cognition Lab based at Lingnan University, Hong Kong is led by Prof. Will Hayward. The research conducted by the Visual Cognition Lab is diverse, ranging from person perception through to post-COVID cognitions and perceptions. Our lab utilises behavioural tasks alongside EEG and eye-tracking to explore our research topics. 

The Visual Cognition Lab is also part of the [Cognitive Science Group](https://cognitive-science.group/) at the Psychology department at Lingnan University.  

<div id="mc_embed_shell">
      <link href="//cdn-images.mailchimp.com/embedcode/classic-061523.css" rel="stylesheet" type="text/css">
  <style type="text/css">
        #mc_embed_signup{background:#fff; false;clear:left; font:14px Helvetica,Arial,sans-serif; width: 600px;}
        /* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
           We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
    <form action="https://github.us22.list-manage.com/subscribe/post?u=546e5e6b8dbb4332447099364&amp;id=b13ee4b014&amp;f_id=0007cce1f0" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank">
        <div id="mc_embed_signup_scroll"><h2>Subscribe</h2>
            <div class="indicates-required"><span class="asterisk">*</span> indicates required</div>
            <div class="mc-field-group"><label for="mce-EMAIL">Email Address <span class="asterisk">*</span></label><input type="email" name="EMAIL" class="required email" id="mce-EMAIL" required="" value=""></div><div class="mc-field-group"><label for="mce-FNAME">First Name </label><input type="text" name="FNAME" class=" text" id="mce-FNAME" value=""></div><div class="mc-field-group"><label for="mce-LNAME">Last Name </label><input type="text" name="LNAME" class=" text" id="mce-LNAME" value=""></div>
        <div id="mce-responses" class="clear foot">
            <div class="response" id="mce-error-response" style="display: none;"></div>
            <div class="response" id="mce-success-response" style="display: none;"></div>
        </div>
    <div aria-hidden="true" style="position: absolute; left: -5000px;">
        /* real people should not fill this in and expect good things - do not remove this or risk form bot signups */
        <input type="text" name="b_546e5e6b8dbb4332447099364_b13ee4b014" tabindex="-1" value="">
    </div>
        <div class="optionalParent">
            <div class="clear foot">
                <input type="submit" name="subscribe" id="mc-embedded-subscribe" class="button" value="Subscribe">
                <p style="margin: 0px auto;"><a href="http://eepurl.com/iTdX2g" title="Mailchimp - email marketing made easy and fun"><span style="display: inline-block; background-color: transparent; border-radius: 4px;"><img class="refferal_badge" src="https://digitalasset.intuit.com/render/content/dam/intuit/mc-fe/en_us/images/intuit-mc-rewards-text-dark.svg" alt="Intuit Mailchimp" style="width: 220px; height: 40px; display: flex; padding: 2px 0px; justify-content: center; align-items: center;"></span></a></p>
            </div>
        </div>
    </div>
</form>
</div>
<script type="text/javascript" src="//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js"></script><script type="text/javascript">(function($) {window.fnames = new Array(); window.ftypes = new Array();fnames[0]='EMAIL';ftypes[0]='email';fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';}(jQuery));var $mcj = jQuery.noConflict(true);</script></div>


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
  image="images/front_page/will_vss.JPG"
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
