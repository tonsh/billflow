#coding=utf-8
''' 封装RequestHandler, 作为应用Handler的基类 '''

import tornado.web
from libs.mako_template import MakoTemplater
from models.user import User

class BaseHandler(tornado.web.RequestHandler):
    ''' 应用Handler的基类 '''

    def get_current_user(self):
        ''' 重写 handler的 get_current_user '''
        user_id = self.get_secure_cookie("user")
        if not user_id:
            return None

        user = User().get_user_by_id(int(user_id))
        return user

    def get_user_locale(self):
        ''' 重写 handler的 get_user_locale '''
        if not self.current_user:
            #Use the Accept-Language header
            return None
        return self.current_user.get("locale", None)

    def render(self, tmpl_name, **context):
        ''' 从写render方法，使用Mako模板引擎实现 '''
        env_context = {
            "current_user": self.current_user,
            "locale":       self.locale,
            "_":            self.locale.translate,
            "static_url":   self.static_url,
        }
        context.update(env_context)
        html = MakoTemplater.render(tmpl_name, **context)
        self.finish(html)

    def request_args(self):
        ''' 处理 Tornado request 返回的List化的参数 '''
        result = {}
        for key in self.request.arguments:
            result[key] = self.get_argument(key)
        return result

    def return_json(self, data={}):
        ''' 响应 Json 数据 '''
        self.set_header('Content-Type', 'application/json')
        self.write(data)
        self.finish()
