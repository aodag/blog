from pyramid.config import Configurator


def includeme(config):
    config.scan(".views")


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    config.include(".")
    return config.make_wsgi_app()
