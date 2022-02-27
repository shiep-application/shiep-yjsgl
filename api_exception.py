from werkzeug.exceptions import HTTPException
import json
from flask import jsonify


class APIException(HTTPException):
    code = 400
    message = 'Sorry, there was an unexpected error(*^v^*)'

    def __init__(self, msg=None, code=None, headers="application/json"):

        self.headers = headers
        if code:
            self.code = code
        if msg:
            self.message = msg
        super().__init__(msg, None)

    def get_body(self, environ=None):  # 这里是将数据改成指定的json格式
        body = dict(
            error_code=self.error_code,
            msg=self.message
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):  # 这里主要是想指定格式  application/json
        return [("Content-Type", self.headers)]


class SHDLDX_LOGIN_FAILED(APIException):
    code = 10001
    message = "统一身份验证出错"
class LOGIN_VALIDATION_FAILED(APIException):
    code = 10002
    message = "学号或密码错误"

class PJ_LESSON_QUERY_FAILED(APIException):
    code = 20001
    message = "评教课程获取出错"
class PJ_TABLE_QUERY_FAILED(APIException):
    code = 20002
    message = "评教表单获取出错"
class PJ_POST_FAILED(APIException):
    code = 20003
    message = "评教提交出错"
    
class DT_QUERY_FAILED(APIException):
    code = 30001
    message = "动态查询出错"
class DT_CITY_QUERY_FAILED(APIException):
    code = 30002
    message = "动态城市查询出错"
class DT_AREA_QUERY_FAILED(APIException):
    code = 30003
    message = "动态区域查询出错"
class DT_POST_FAILED (APIException):
    code = 30004
    message = "动态提交出错"

err_list = {
    SHDLDX_LOGIN_FAILED, LOGIN_VALIDATION_FAILED,
    PJ_LESSON_QUERY_FAILED, PJ_TABLE_QUERY_FAILED, PJ_POST_FAILED,
    DT_QUERY_FAILED, DT_CITY_QUERY_FAILED, DT_AREA_QUERY_FAILED, DT_POST_FAILED
}

def custom_exception_handlers(app):
    for cls in err_list:
        @app.errorhandler(cls)
        def _(exc):
            return jsonify({"err_code": exc.code, "err_msg": exc.message})


