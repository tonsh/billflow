# coding=utf-8
''' 应用服务配置 '''

import tornado.web
import tornado.ioloop
from handlers.home_handler import HomeHandler
from handlers.home_handler import LoginHandler
from handlers.home_handler import RegisterHandler

settings = {
    "login_url": "/login",
}

application = tornado.web.Application([
    (r"/",      HomeHandler),
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
