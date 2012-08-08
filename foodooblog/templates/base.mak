## base.html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:tal="http://xml.zope.org/namespaces/tal">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title><%block name="title"/> - FooDooBlog</title>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/jquery-ui.min.js"></script>
    <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/blitzer/jquery-ui.css" type="text/css" />
  </head>
  <body>
    <div class="header">
      <%include file="header.mak"/>
    </div>

    <div class="body">
     ${self.body()}
    </div>

    <div class="footer">
      <%block name="footer">
      this is the footer
</%block>
</div>
</body>
</html>
