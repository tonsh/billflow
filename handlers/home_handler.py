# coding=utf-8
''' 首页 RequestHandler '''

import tornado.web
from handlers.base_handler import BaseHandler
from libs.bill_exception import BillException
from models.user import User

class HomeHandler(BaseHandler):
    ''' 首页 '''
    def get(self):
        ''' 如果用户未登录，跳转至登录页面 '''
        self.render("home.html")

class SettingHandler(BaseHandler):
    ''' 个人设置 '''
    @tornado.web.authenticated
    def get(self):
        from libs.utils import row2dict
        self.return_json(row2dict(self.current_user))


class LoginHandler(BaseHandler):
    ''' 登录 '''
    def get(self):
        if self.current_user:
            self.redirect("/setting")
        else:
            self.render("login.html")

    def post(self):
        try:
            args = self.request_args()
            user = User().get_login_user(args)
            self.set_secure_cookie("user", str(user.id))
            self.redirect("/setting")
        except BillException as error:
            self.return_json(error.info())


class LogoutHandler(BaseHandler):
    ''' 取消登录 '''
    def get(self):
        self.set_secure_cookie("user", "")
        self.redirect("/")

class RegisterHandler(BaseHandler):
    '''注册 '''
    def get(self):
        self.render("register.html")

    def post(self):
        try:
            args = self.request_args()
            if args.get("password") != args.get("repwd"):
                raise BillException(101)

            user = User().create(args)
            self.set_secure_cookie("user", str(user.id))
            self.redirect("/setting")
        except BillException as error:
            self.return_json(error.info())
