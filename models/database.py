#conding=utf-8
''' 数据库连接基类 '''

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings.conf import MYSQL_MAP 

Base = declarative_base()

class Database(object):
    ''' 数据库连接基类 '''
    _instance = None

    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://%s:%s@%s/%s" % (
                MYSQL_MAP['user'],
                MYSQL_MAP['pwd'],
                MYSQL_MAP['host'],
                MYSQL_MAP['database'],
            ),
            encoding=MYSQL_MAP['encoding'],
            echo=MYSQL_MAP['echo'],
        )

        self.session = scoped_session(sessionmaker(bind=self.engine))

    def create_db(self):
        Base.metadata.create_all(self.engine)

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = Database()

        return cls._instance
