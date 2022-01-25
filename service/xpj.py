from service.shdldxlogin import *
from api_exception import *
from urllib.parse import urlencode


def lesson_query_service(username, password):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 课程查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/pygl/wsjxpjlist"
    # print(grade_query_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    response = requests.post(grade_query_url, headers=headers, allow_redirects=False)
    # print(response.text)
    return_list = []
    for item in json.loads(response.text):
        shaped_item = {"bjid": item["bjid"], "jsbh": item["jsbh"], "kcmc": item["kcmc"], "jsxm": item["jsxm"], "kssj": item["kssj"], "jssj": item["jssj"], "sfpj": item["sfpj"], "yxpj": item["yxpj"]}
        return_list.append(shaped_item)
    print(return_list)
    return return_list



def pj_query_service(username, password, bjid, jsbh):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 评教问卷查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/pygl/wsjxpj_pj_load?bjid=" + bjid + "&jsbh=" + jsbh
    # print(grade_query_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    response = requests.get(grade_query_url, headers=headers, allow_redirects=False)
    print(response.text)

    return response.text


def post_pj_service(username, password, bjid, jsbh, pj_json):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 评教提交查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/pygl/wsjxpj_pj_save"

    pj_json = json.dumps(pj_json)

    data = {"bjid": bjid, "jsbh": jsbh, "json": pj_json}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"] +
                  "ASP.NET_SessionId=; __LOGINCOOKIE__=;"
    }
    data = urlencode(data)
    response = requests.post(grade_query_url, data=data, headers=headers, allow_redirects=False)
    return response.text  # 如果返回的是1就是评教成功



# lesson_query_service("y21207011", "wykbjdy999")
# pj_query_service("y21207011", "wykbjdy999", "be74bd70-0570-43ad-9de2-38b00c8c9d0a", "2008000012")

# pj_json = [
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "1", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "2", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "3", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "4", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "5", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "6", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "7", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "8", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "9", "zt": "1", "df": "8.0"},
#     {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "10", "zt": "1", "df": "8.0"}
# ]
#
# post_pj("y21207011", "wykbjdy999", bjid="2f33246b-00bb-4067-9d0b-f682b9c06fab", jsbh="2020010004", pj_json=pj_json)





