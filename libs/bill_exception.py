#coding=utf-8
''' (错误码)异常处理类 '''

from settings.error_code import ERROR_CODES

class BillException(Exception):
    ''' (错误码)异常处理类 '''
    def __init__(self, error_code):
        self.error_code = int(error_code)
        default_msg = "Error: %i" % error_code
        self.message = ERROR_CODES.get(error_code, default_msg)

    def info(self):
        ''' 返回错误信息 '''
        return {
            "error_code": self.error_code,
            "message": self.message,
        }
