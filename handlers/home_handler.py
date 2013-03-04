# coding=utf-8
''' 首页 RequestHandler '''

import tornado.web
from handlers.base_handler import BaseHandler
from libs.bill_exception import BillException

class HomeHandler(tornado.web.RequestHandler):
    ''' 首页 '''
    @tornado.web.authenticated
    def get(self):
        ''' 如果用户未登录，跳转至登录页面 '''
        self.write('Hello Home')


class LoginHandler(tornado.web.RequestHandler):
    ''' 登录 '''
    def get(self):
        self.write('Login')


class RegisterHandler(BaseHandler):
    '''注册 '''
    def get(self):
        self.render('register.html')

    def post(self):
        from models.user import User
        from libs.utils import row2dict

        try:
            args = self.request_args()
            if args.get('password') != args.get('repwd'):
                raise BillException(101)

            user = User().create(args)
            self.return_json(row2dict(user))
        except BillException as error:
            self.return_json(error.info())
