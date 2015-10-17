from pyramid.config import Configurator


def includeme(config):
    config.add_route("blog.root", "/")
    config.add_route("blog.entries", "/entries")
    config.add_route("blog.edit", "/manage/edit")
    config.add_route("entry.create", "/manage/entries")
    config.scan(".views")
    config.scan(".layouts")


def main(global_conf, **settings):
    config = Configurator(settings=settings,
                          root_factory=".resources.BlogResource")
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    config.include(".")
    return config.make_wsgi_app()
