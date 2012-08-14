<%inherit file="base.mak"/>

<%block name="title">Add new post</%block>

<form action="${save_url}" method="post">
  <textarea name="title" rows="1" cols="60" placeholder="Post title"></textarea><br/>
  <textarea name="body" rows="10" cols="60" placeholder="Blog post body"></textarea><br/>
  <input type="submit" name="form.submitted" value="Save"/>
</form>
