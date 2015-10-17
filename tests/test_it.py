import pytest
import webtest
from testfixtures import compare, Comparison as C


settings = {
    "pyramid.includes": [
        "pyramid_jinja2",
        "pyramid_sqlalchemy",
        "pyramid_layout",
        "pyramid_deform",
    ],
    "sqlalchemy.url": "sqlite:///",
}


@pytest.fixture
def app(request):
    from blog import main
    from blog import models
    models.Session.remove()
    app = main({}, **settings)
    app = webtest.TestApp(app)
    engine = models.Session.bind
    models.BaseObject.metadata.create_all(bind=engine)

    def fin():
        import transaction
        transaction.abort()

    request.addfinalizer(fin)
    return app


@pytest.fixture
def default_blog(app):
    from blog import models
    blog = models.Blog(name="default",
                       title="default blog",
                       description="this is default blog")
    models.Session.add(blog)
    return blog


def test_index(app):
    res = app.get("/")
    assert res


def test_edit_blog(app, default_blog):
    res = app.get("/manage/edit")
    res.form["title"] = "edited blog title"
    res.form["description"] = "description"
    res = res.form.submit('save')
    assert res.location == 'http://localhost/'
    assert default_blog.title == "edited blog title"
    assert default_blog.description == "description"

    res = app.get("/")
    assert "edited blog title" in res


def test_add_entry(app, default_blog):
    from blog.models import Entry
    res = app.get("/manage/entries")
    res.form["name"] = "first-entry"
    res.form["title"] = "this is first entry"
    res.form["description"] = "entry description"
    res.form["date"] = "2015-10-11"
    res = res.form.submit('save')

    assert res.location == 'http://localhost/'

    assert len(default_blog.entries) == 1
    compare(default_blog.entries[0], C(Entry))

    res = app.get("/")
    assert "this is first entry" in res
