from service.shdldxlogin import *
from api_exception import *


def dt_query_service(username, password):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 动态查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/yggl/yjsdtgl_list"
    # print(grade_query_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    response = requests.post(grade_query_url, headers=headers, allow_redirects=False)
    # print(response.text)
    return response.text


def city_query_service(username, password, province_id):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 城市查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/yggl/getcity"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    data = {"province": province_id}
    response = requests.post(grade_query_url, headers=headers, data=data, allow_redirects=False)
    # print(response.text)
    return response.text


def area_query_service(username, password, city_id):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 区域查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/yggl/getArea"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    data = {"city": city_id}
    response = requests.post(grade_query_url, headers=headers, data=data, allow_redirects=False)
    # print(response.text)
    return response.text


def post_xc_service(username, password, xc_json):
    # 统一身份验证
    try:
        cookies, url_prefix = shdldxlogin(username, password)
    except LOGIN_VALIDATION_FAILED:
        raise LOGIN_VALIDATION_FAILED
    except Exception:
        raise SHDLDX_LOGIN_FAILED

    # 区域查询接口
    CASTGC = cookies["CASTGC"]
    _ = CASTGC.split()
    grade_query_url = url_prefix + "student/yggl/yjsdtgl_addxc_save"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"] +
                  "; __SINDEXCOOKIE__=" + cookies["__SINDEXCOOKIE__"]
    }
    data = {"json": json.dumps(xc_json)}
    response = requests.post(grade_query_url, headers=headers, data=data, allow_redirects=False)
    # print(response.text)
    return response.text  # 添加成功的返回 {"zt":"1"}


# dt_query_service("y21207011", "wykbjdy999")
# city_query_service("y21207011", "wykbjdy999", province_id=33)
# area_query_service("y21207011", "wykbjdy999", city_id=3301)

xc_json = {
    "xcid": "7128",  # 行程id
    "bdsj": "2022-01-25 19:17:04",  # 变动时间

    "xclb": "03",  # 行程类别：1在校；2离沪在校；3离沪

    "provinceId": "33",
    "cityId": "3301",
    "areaId": "330101",
    "jdxx": "1",  # 街道详细

    # 此参数只用于离沪行程
    "jtfs": "03",  # 交通方式：1自驾；2大巴；3火车；4飞机

    # 以下两个参数只有在交通方式为火车/飞机才使用
    "ccxx": "xxxxxx",  # 初次详细
    "hcxx": "xxxxxx",  # 换乘详细
}
post_xc_service("y21207011", "wykbjdy999", xc_json)