from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import (
    DBSession,
    Post,
    title_to_name,
    )

from .search import gen_search_bar
from .surroundings import environment_factory

class PostView(object):
    """This class manages views related to posts."""

    @view_config(route_name='view_post', renderer='post-view.mak')
    def view(request):
        post = DBSession.query(Post).filter(Post.name==request.matchdict['postname']).first()
        post.view_count += 1
        return environment_factory(post=post)

    @view_config(route_name='edit_post', renderer='edit.mak')
    def edit(request):
        """Edit view for the post."""
        if 'form.submitted' in request.params:
            # delete old post
            title = request.params['title']
            name = title_to_name(title)

            if not name or DBSession.query(Post).filter(Post.name==name).count():
                # this should be a popup ajaxy box
                return Response("Name %s is in use, choose a different title" % name, content_type='text/plain', status_int=500)

        body = request.params['body']
        post = Post(title, body, name)
        DBSession.add(post)
        return HTTPFound(location = request.route_url('view_post', postname=name))

        save_url = request.route_url('edit_post')
        post = DBSession.query(Post).filter(Post.name==name).first()
        return environment_factory(post=post, save_url=save_url)


    @view_config(route_name="delete_item", renderer="json")
    def delete_item(request):
        """This is a completely ajaxified way of deleting posts."""
        if request.json_body[u'type'] == u'post':
            if DBSession.query(Post).filter(Post.name==request.json_body[u'name']).delete() == 1:
                return {"deletion_status":"success"}
            import ipdb; impdb.set_trace()
            return {"deletion_status":"error"}

    @view_config(route_name='new_post', renderer='edit.mak')
    def add_post(request):
        """Show edit form if no form is submitted, if a form Is submitted,
        add the post and redirect to view it!"""
        if 'form.submitted' in request.params:
            title = request.params['title']
            name = title_to_name(title)

            if not name or DBSession.query(Post).filter(Post.name==name).count():
                # this should be a popup ajaxy box
                return Response("Name %s is in use, choose a different title" % name, content_type='text/plain', status_int=500)

            body = request.params['body']
            post = Post(title, body, name)
            DBSession.add(post)
            return HTTPFound(location = request.route_url('view_post', postname=name))

        save_url = request.route_url('new_post')
        post = Post('')
        return environment_factory(post=post, save_url=save_url)

@view_config(route_name='home', renderer='homepage.mak')
def post_list(request):
    posts = DBSession.query(Post).all()
    return environment_factory(posts=posts, title=u"Home", search_bar=gen_search_bar())


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_FooDooBlog_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
