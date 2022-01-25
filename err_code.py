ShdldxLOGIN_FAILED = {"err_code": 10001, "err_msg": "统一身份验证出错"}
LOGIN_VALIDATION_FAILED = {"err_code": 10002, "err_msg": "学号或密码错误"}
PJ_LESSON_QUERY_FAILED = {"err_code": 20001, "err_msg": "评教课程获取出错"}
PJ_TABLE_QUERY_FAILED = {"err_code": 20002, "err_msg": "评教表单获取出错"}
PJ_POST_FAILED = {"err_code": 20003, "err_msg": "评教提交出错"}


class BussinessException:
    err_code = 10000
    err_msg = "ops, something seem to go wrong"

    def __init__(self, err_json):
        self.err_code = err_json["err_code"]
        self.err_msg = err_json["err_msg"]


