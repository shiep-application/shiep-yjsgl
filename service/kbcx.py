from service.shdldxlogin import *
from api_exception import *
from urllib.parse import urlencode


def kb_query_service(username, password, termcode):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 课表查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    kb_query_url = url_prefix + "student/pygl/py_kbcx_ew"
    # print(grade_query_url)
    data = {"kblx": "xs", "termcode": termcode}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    response = requests.post(kb_query_url, data=data, headers=headers, allow_redirects=False)
    return json.loads(response.text)["rows"]
