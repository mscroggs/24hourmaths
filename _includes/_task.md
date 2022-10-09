<center><img src='/assets/img/taskm.jpg' width="80" style="margin:0px;padding:0px;border:none;box-shadow:none;-webkit-box-shadow:none;-moz-box-shadow:none;-o-box-shadow:none;-ms-box-shadow:none;"><br /><strong>{{ include.task | markdownify }}</strong></center>

{% if {{include.more}} %}
<div style='font-size:80%'>{{ include.more | markdownify }}</div>
{% endif %}

<div style="height:50px">&nbsp;</div>
