from . import models


class BlogResource(object):
    def __init__(self, request):
        self.request = request
        self.blog_name = request.registry.settings.get("blog.name", "default")

    @property
    def blog(self):
        return models.Blog.query.filter(
            models.Blog.name == self.blog_name,
        ).first()
