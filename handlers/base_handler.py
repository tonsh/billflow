#coding=utf-8
''' 封装RequestHandler, 作为应用Handler的基类 '''

import tornado.web
from libs.mako_template import MakoTemplater

class BaseHandler(tornado.web.RequestHandler):
    ''' 应用Handler的基类 '''

    def render(self, tmpl_name, **context):
        ''' 从写render方法，使用Mako模板引擎实现 '''
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
