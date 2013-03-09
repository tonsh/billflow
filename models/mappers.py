#coding=utf-8
''' Tables basic models '''

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models.database import Base
from models.database import Database

class UserMapper(Base):
    ''' 用户表结构 '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, doc='用户ID')
    name = Column(String(30), nullable=True, unique=True, doc='用户名')
    password = Column(String(128), nullable=False, doc='用户密码')
    locale = Column(String(10), nullable=False, default='zh_CN', doc='语言信息')

    def __repr__(self):
        return "<User('%s')>" % (self.name)

Database.instance().create_db()
