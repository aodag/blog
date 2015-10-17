from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Unicode,
    UnicodeText,
)
from sqlalchemy.orm import (
    relationship,
)

from pyramid_sqlalchemy import (
    BaseObject,
    Session,
)


class Blog(BaseObject):
    __tablename__ = 'blogs'
    query = Session.query_property()
    blog_id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    title = Column(UnicodeText, nullable=False)
    description = Column(UnicodeText, nullable=False)


class Entry(BaseObject):
    __tablename__ = 'entries'
    query = Session.query_property()
    entry_id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey('blogs.blog_id'))
    blog = relationship('Blog', backref="entries")
    name = Column(Unicode(255), nullable=False)
    title = Column(UnicodeText, nullable=False)
    description = Column(UnicodeText, nullable=False)
    date = Column(Date, nullable=False)
