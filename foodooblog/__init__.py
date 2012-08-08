from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('delete_item','/delete')
    config.add_route('new_post','/create')
    config.add_route('view_post','/{postname}')
    config.add_route('edit_post','/{postname}/edit')
    config.scan()
    return config.make_wsgi_app()