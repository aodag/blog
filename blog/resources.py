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

    def add_blog(self, name, title, description):
        blog = models.Blog(name=name,
                           title=title,
                           description=description)
        models.Session.add(blog)

    def __getitem__(self, name):
        return models.Entry.query.filter(
            models.Blog.name == self.blog_name,
            models.Entry.blog_id == models.Blog.blog_id,
            models.Entry.name == name,
        ).first()
