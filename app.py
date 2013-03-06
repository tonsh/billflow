# coding=utf-8
''' 应用服务配置 '''

import tornado.web
import tornado.ioloop
import tornado.locale
from handlers.home_handler import HomeHandler
from handlers.home_handler import LoginHandler
from handlers.home_handler import RegisterHandler
from handlers.home_handler import SettingHandler

settings = {
    "login_url": "/login",
    "cookie_secret": "c5586ff9f6ac5211198e37c46154b26e",
}

application = tornado.web.Application([
    (r"/",      HomeHandler),
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler),
    (r"/setting", SettingHandler),
], **settings)

if __name__ == "__main__":
    # List supported locale run `print(locale.get_supported_locales())`
    tornado.locale.load_gettext_translations("./locale", "lang")

    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
