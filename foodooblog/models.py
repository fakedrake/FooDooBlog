from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

def title_to_name(title):
    return ''.join(c for c in title.lower().replace(" ","_") if c.isdigit() or c.islower() or c == '_')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    title = Column(Text)
    body = Column(Integer)

    def __init__(self, title, body='', name=None):
        if name is None:
            name = title_to_name(title)

        self.name = name
        self.title = title
        self.body = body
