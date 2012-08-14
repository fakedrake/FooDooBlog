<%inherit file="base.mak"/>

<%block name="title">Home</%block>


<ul class="post-list">
  % for post in posts:
  <li class="post-list-item">
    <a class="post-view-link" href="${request.application_url}/${post.name}">
      <div id="${post.name}" class="post-title">
	<span>${post.title}</span>
      </div>
    </a>
  </li>

  <!--   <li> -->
  <!--     <a href="${request.application_url}/${post.name}" class="post-entry" id="${post.name}"> -->
  <!--       <span class="ca-icon">A</span> -->
  <!--       <div class="ca-content"> -->
  <!--         <h2 class="ca-main">${post.title}</h2> -->
  <!--         <\!-- <h3 class="ca-sub">${post.title}</h3> -\-> -->
  <!--       </div> -->
  <!--       <div class="post-menu"> -->
  <!-- 	<a href="#" class="delete-link">Delete</a> -->
  <!--       </div> -->
  <!--     </a> -->
  <!--   </li> -->
  % endfor
</ul>
<a href="${request.application_url}/create" class="create-post-link">Add new post</a>


<script type="text/javascript" src="${request.static_url('foodooblog:static/homepage.js')}"></script>
