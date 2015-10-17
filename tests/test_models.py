import pytest


class TestBlog(object):
    @pytest.fixture
    def target(self):
        from blog.models import Blog
        return Blog

    def test_init(self, target):
        blog = target()
        assert blog.entries == []


class TestEntry(object):
    @pytest.fixture
    def target(self):
        from blog.models import Entry
        return Entry

    def test_init(self, target):
        entry = target()
        assert entry.blog is None
