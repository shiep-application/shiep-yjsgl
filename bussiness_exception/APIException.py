from werkzeug.exceptions import HTTPException
import json


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
