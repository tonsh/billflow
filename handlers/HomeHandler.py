#coding=utf-8
''' 首页 RequestHandler '''

import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    ''' 首页 '''
    def get(self):
        self.write('Hello Home')
