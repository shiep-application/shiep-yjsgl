import re
import json
from flask import Flask
from flask import request
from service.grade_query import *
from service.xpj import *
from err_code import *


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
        raise ShdldxLOGIN_FAILED
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
        raise ShdldxLOGIN_FAILED
    except Exception:
        raise PJ_TABLE_QUERY_FAILED
    return json.dumps(result)


@app.route('/post_pj', methods=['POST'])
def post_pj():
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
        raise ShdldxLOGIN_FAILED
    except Exception:
        raise PJ_POST_FAILED
    return json.dumps(result)


if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=7788
    )