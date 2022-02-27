from bussiness_exception.APIException import *


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
