import re
import json
from flask import Flask
from flask import request
from service.grade_query import *


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Word'


@app.route('/grade_query', methods=['GET'])
def grade_query():
    # username = request.json.get("username").strip()
    # password = request.json.get("password").strip()

    username = request.args.get("username")
    password= request.args.get("password")

    result = grade_query_service(username, password)

    return json.dumps(result)


if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=7788
    )