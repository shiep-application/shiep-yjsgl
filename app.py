import re
import json
from flask import Flask
from flask import request
from service.grade_query import *
from service.xpj import *
from service.dtsq import *


app = Flask(__name__)
custom_exception_handlers(app)


@app.route('/')
def index():
    return 'Hello Word'


@app.route('/grade_query', methods=['POST'])
def grade_query():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()

    result = grade_query_service(username, password)
    return json.dumps(result)


@app.route('/pj_lesson_query', methods=['POST'])
def pj_lesson_query():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()

    try:
        result = lesson_query_service(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except SHDLDX_LOGIN_FAILED:
        raise SHDLDX_LOGIN_FAILED
    except Exception:
        raise PJ_LESSON_QUERY_FAILED
    return json.dumps(result)


@app.route('/pj_table_query', methods=['POST'])
def pj_table_query():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    bjid = request.json.get("bjid").strip()
    jsbh = request.json.get("jsbh").strip()

    try:
        result = pj_query_service(username, password, bjid, jsbh)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except SHDLDX_LOGIN_FAILED:
        raise SHDLDX_LOGIN_FAILED
    except Exception:
        raise PJ_TABLE_QUERY_FAILED
    return json.dumps(result)


@app.route('/pj_post', methods=['POST'])
def pj_post():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    bjid = request.json.get("bjid").strip()
    jsbh = request.json.get("jsbh").strip()
    pj_json = request.json.get("pj_json").strip()

    try:
        result = post_pj_service(username, password, bjid, jsbh, pj_json)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except SHDLDX_LOGIN_FAILED:
        raise SHDLDX_LOGIN_FAILED
    except Exception:
        raise PJ_POST_FAILED
    return json.dumps(result)


@app.route('/dt_query', methods=['POST'])
def dt_query():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()

    try:
        result = dt_query_service(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except SHDLDX_LOGIN_FAILED:
        raise SHDLDX_LOGIN_FAILED
    except Exception:
        raise DT_QUERY_FAILED
    return json.dumps(result)


@app.route('/dt_city_query', methods=['POST'])
def dt_city_query():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    province_id = request.json.get("province_id").strip()

    try:
        result = city_query_service(username, password, province_id)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except SHDLDX_LOGIN_FAILED:
        raise SHDLDX_LOGIN_FAILED
    except Exception:
        raise DT_CITY_QUERY_FAILED
    return json.dumps(result)


@app.route('/dt_area_query', methods=['POST'])
def dt_area_query():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    city_id = request.json.get("city_id").strip()

    try:
        result = area_query_service(username, password, city_id)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except SHDLDX_LOGIN_FAILED:
        raise SHDLDX_LOGIN_FAILED
    except Exception:
        raise DT_AREA_QUERY_FAILED
    return json.dumps(result)


@app.route('/dt_post', methods=['POST'])
def dt_post():
    username = request.json.get("username").strip()
    password = request.json.get("password").strip()
    xc_json = request.json.get("xc_json").strip()

    try:
        result = post_xc_service(username, password, xc_json)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except SHDLDX_LOGIN_FAILED:
        raise SHDLDX_LOGIN_FAILED
    except Exception:
        raise DT_POST_FAILED
    return json.dumps(result)


if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=7788
    )