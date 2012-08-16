<%inherit file="base.mak"/>

<%block name="title">${post.title}</%block>

<div class="post">
  <div class="post-title">
    <h3>${post.title}</h3>
  </div>
  <div class="post-body">
    ${post.body}
  </div>
  <div class="post-properties">Views: ${post.view_count}</div>
</div>
