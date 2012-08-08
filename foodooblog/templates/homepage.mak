<%inherit file="base.mak"/>

<%block name="title">Home</%block>


<div class="posts">
  <ul>
% for post in posts:
    <li><div id="${post.name}" class="post-list-item"> ${loop.index}: <a class="postlink" href="${request.application_url}/${post.name}"> ${post.title}</a></div></li>
% endfor
  </ul>
</div>
<a href="${request.application_url}/create">Add new post</a>


<script type="text/javascript" src="${request.static_url('foodooblog:static/homepage.js')}"></script>
