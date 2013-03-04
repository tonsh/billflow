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
        from models.mappers import UserMapper

        try:
            args = self.request_args()
            if args.get('pwd') != args.get('repwd'):
                raise BillException(101)
            self.return_json(args)
        except BillException as error:
            self.return_json(error.info())
