#coding=utf-8
''' 用户模型 '''

import hashlib
from models.mappers import UserMapper
from models.database import Database
from libs.bill_exception import BillException


class User(object):
    ''' 用户相关 '''
    def __init__(self):
        self.db = Database.instance()
        self.session = self.db.get_session()

    def get_user_by_id(self, user_id):
        return self.session.query(UserMapper).filter_by(id=user_id).first()

    def get_login_user(self, user):
        return self.session.query(UserMapper).filter_by(
                    name=user.get('name', ''),
                    password=self.check_pwd(user.get('password', '')),
                ).first()

    def create(self, user):
        ''' 添加一个新用户 '''
        new = {
            'name': self.check_name(user.get('name', '')),
            'password': self.check_pwd(user.get('password', '')),
            'locale': self.check_locale(user.get('locale', 'zh_CN')),
        }
        save_user = UserMapper(**new)
        self.session.add(save_user)
        self.session.commit()

        return save_user

    def check_name(self, name):
        ''' 用户名称验证 '''
        name = name.strip()
        if not name:
            raise BillException(102)

        ucount = self.session.query(UserMapper).filter_by(name=name).count()
        if ucount > 0:
            raise BillException(104)

        return name

    def check_pwd(self, pwd):
        ''' 密码验证 '''
        pwd = pwd.strip()
        if not pwd:
            raise BillException(103)

        return hashlib.new("md5", pwd.encode('utf-8')).hexdigest()

    def check_locale(self, locale):
        ''' 地域验证 '''
        if locale not in ['zh_CN', 'en_US']:
            locale = 'zh_CN'

        return locale
