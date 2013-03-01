# coding=utf-8
''' 首页 RequestHandler '''

import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    ''' 首页 '''
    def get(self):
        # 如果用户未登录，跳转至登录页面
        if not self.current_user:
            self.redirect('/login')
        else:
            self.write('Hello Home')


class LoginHandler(tornado.web.RequestHandler):
    ''' 登录 '''
    def get(self):
        self.write('Login')