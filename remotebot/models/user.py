from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm
from datetime import datetime, timedelta
from hashlib import sha1
import uuid
from sqlalchemy.ext.hybrid import hybrid_property, Comparator
from .. import configuration
Base = declarative_base()


class _PasswordHashedComparator(Comparator):
    def __init__(self, password_hashed):
        self.password_hashed = password_hashed

    def __eq__(self, other):
        return self.password_hashed == sha1(other.encode()).hexdigest()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hashed = Column(String)
    api_key = Column(String)
    api_key_expiration = Column(DateTime)

    @hybrid_property
    def password(self):
        raise NotImplementedError("Comparison only supported via the database")

    @password.setter
    def password(self, value):
        self.password_hashed = sha1(value.encode()).hexdigest()

    @password.comparator
    def password(cls):
        return _PasswordHashedComparator(cls.password_hashed)

    @classmethod
    def login(cls, username, password, session):
        try:
            user = session.query(User).filter(User.username == username)\
                                      .filter(User.password == password).one()
        except sqlalchemy.orm.exc.NoResultFound:
            return None

        return user

    def api_key_expired(self):
        return self.api_key_expiration - datetime.now() < timedelta()

    def renew_api_key(self):
        self.api_key_expiration =\
            datetime.now() + configuration.api_key_expiration
        self.api_key = uuid.uuid4()
        return self.api_key