import datetime
from service.shdldxlogin import *
from api_exception import *


def grade_query_service(username, password):
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 成绩查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/pygl/xscjcx_list?_=" + str(datetime.datetime.now().timestamp() * 1000)
    # print(grade_query_url)
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    response = requests.post(grade_query_url, headers=headers, allow_redirects=False)
    # print(response.text)
    xwklist = json.loads(response.text)["xwklist"]
    fxwklist = json.loads(response.text)["fxwklist"]
    xftj = json.loads(response.text)["xftj"]

    # for item in xwklist:
    #     print(item)
    # for item in fxwklist:
    #     print(item)
    # for item in xftj:
    #     print(item)

    return {"xwklist": xwklist, "fxwklist": fxwklist, "xftj": xftj}
