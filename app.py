# coding=utf-8
''' 应用服务配置 '''

import tornado.web
import tornado.ioloop
from handlers.HomeHandler import HomeHandler
from handlers.HomeHandler import LoginHandler

settings = {
    "login_url": "/login",
}

application = tornado.web.Application([
    (r"/",      HomeHandler),
    (r"/login", LoginHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
