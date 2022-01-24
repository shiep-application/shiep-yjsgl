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


def custom_exception_handlers(app):
    for cls in {SHDLDX_LOGIN_FAILED, LOGIN_VALIDATION_FAILED}:
        @app.errorhandler(cls)
        def _(exc):
            return jsonify({"code": exc.code, "message": exc.message})


