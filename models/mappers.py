#codin=utf-8
''' Tables basic models '''

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models.database import Base
from models.database import Database

class UserMapper(Base):
    ''' 用户表结构 '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=True)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return "<User('%s')>" % (self.name)

Database.instance().create_db()
