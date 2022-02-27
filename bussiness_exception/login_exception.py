from bussiness_exception.APIException import *

class SHDLDX_LOGIN_FAILED(APIException):
    code = 10001
    message = "统一身份验证出错"
class LOGIN_VALIDATION_FAILED(APIException):
    code = 10002
    message = "学号或密码错误"