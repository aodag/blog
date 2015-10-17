from colanderalchemy import SQLAlchemySchemaNode
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid_deform import FormView
from .models import Blog, Entry


@view_config(route_name="blog.root",
             renderer='templates/index.html')
def index(request):
    return dict(blog=request.context.blog)


@view_config(route_name="blog.entry",
             renderer='templates/entry.html')
def entry(request):
    entry_name = request.matchdict['name']
    entry = request.context[entry_name]
    return dict(entry=entry)


@view_config(route_name="blog.edit",
             renderer='templates/form.html')
class BlogFormView(FormView):
    schema = SQLAlchemySchemaNode(Blog,
                                  includes=['title', 'description'])
    buttons = ('save',)

    def appstruct(self):
        blog = self.blog
        return {
            "title": blog.title,
            "description": blog.description,
        }

    @property
    def context(self):
        return self.request.context

    @property
    def blog(self):
        return self.context.blog

    def save_success(self, values):
        blog = self.blog
        for k, v in values.items():
            setattr(blog, k, v)
        location = self.request.route_url('blog.root')
        return HTTPFound(location=location)


@view_config(route_name="entry.create",
             renderer='templates/form.html')
class EntryFormView(FormView):
    schema = SQLAlchemySchemaNode(Entry,
                                  includes=[
                                      "name",
                                      "title",
                                      "description",
                                      "date",
                                  ])
    buttons = ('save',)

    @property
    def context(self):
        return self.request.context

    @property
    def blog(self):
        return self.context.blog

    def save_success(self, values):
        blog = self.blog
        entry = Entry(**values)
        blog.entries.append(entry)
        location = self.request.route_url('blog.root')
        return HTTPFound(location=location)
