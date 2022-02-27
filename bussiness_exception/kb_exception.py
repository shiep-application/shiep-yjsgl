from bussiness_exception.APIException import *


class KB_QUERY_FAILED(APIException):
    code = 30001
    message = "课表查询出错"
