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
