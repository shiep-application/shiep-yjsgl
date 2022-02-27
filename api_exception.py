from flask import jsonify
from bussiness_exception.login_exception import *
from bussiness_exception.dt_exception import *
from bussiness_exception.kb_exception import *
from bussiness_exception.pj_exception import *


err_list = {
    SHDLDX_LOGIN_FAILED, LOGIN_VALIDATION_FAILED,
    PJ_LESSON_QUERY_FAILED, PJ_TABLE_QUERY_FAILED, PJ_POST_FAILED,
    DT_QUERY_FAILED, DT_CITY_QUERY_FAILED, DT_AREA_QUERY_FAILED, DT_POST_FAILED,
    KB_QUERY_FAILED
}


def custom_exception_handlers(app):
    for cls in err_list:
        @app.errorhandler(cls)
        def _(exc):
            return jsonify({"err_code": exc.code, "err_msg": exc.message})


