from bussiness_exception.APIException import *


class PJ_LESSON_QUERY_FAILED(APIException):
    code = 20001
    message = "评教课程获取出错"
class PJ_TABLE_QUERY_FAILED(APIException):
    code = 20002
    message = "评教表单获取出错"
class PJ_POST_FAILED(APIException):
    code = 20003
    message = "评教提交出错"