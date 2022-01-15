import requests
from bs4 import BeautifulSoup


def shdldxlogin(username, password):
    # get请求统一身份验证页面
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36'
    }
    ids_url = "http://ids.shiep.edu.cn/authserver/login?service=http://yjsgl.shiep.edu.cn/gmis5/oauthLogin/shdldxlogin"
    response = requests.post(ids_url, headers=headers)
    cookie = response.headers['Set-Cookie'].split(";")[0]
    # print(cookie)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    lt = soup.find('form').find_all('input', type="hidden")[0]["value"]
    dllt = soup.find('form').find_all('input', type="hidden")[1]["value"]
    execution = soup.find('form').find_all('input', type="hidden")[2]["value"]
    _eventId = soup.find('form').find_all('input', type="hidden")[3]["value"]
    rmShown = soup.find('form').find_all('input', type="hidden")[4]["value"]

    # 统一身份认证post请求（第一次302）
    data = {
        'username': username,
        'password': password,
        'lt': lt,
        'dllt': dllt,
        'execution': execution,
        '_eventId': _eventId,
        'rmShown': rmShown,
    }
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': cookie
    }
    response = requests.post(ids_url, headers=headers1, data=data, allow_redirects=False)
    cookies1 = response.cookies
    cookies = {}
    for cookie in cookies1:
        cookies[cookie.name] = cookie.value
    # print(cookies)
    url2 = response.headers["Location"]
    # print(url2)

    # 统一身份认证post请求（第二次302）
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"]
    }
    response2 = requests.post(url2, headers=headers2, data=data, allow_redirects=False)
    cookies2 = response2.cookies
    for cookie in cookies2:
        cookies[cookie.name] = cookie.value
    # print(cookies)
    url3 = response2.headers["Location"]
    # print(url3)

    # 统一身份认证post请求（第三次302）
    headers3 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"]
    }
    response3 = requests.post(url3, headers=headers3, data=data, allow_redirects=False)
    url4 = "http://yjsgl.shiep.edu.cn/" + response3.headers["Location"]
    # print(url4)
    url_prefix = url4.split("oauthLogin")[0]
    # print(url_prefix)

    # 统一身份认证post请求（第四次302）
    headers4 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36',
        'Cookie': "iPlanetDirectoryPro=" + cookies["iPlanetDirectoryPro"] +
                  "; .ASPXAUTH=" + cookies[".ASPXAUTH"]
    }
    response4 = requests.post(url4, headers=headers4, data=data, allow_redirects=False)
    cookies4 = response4.cookies
    for cookie in cookies4:
        cookies[cookie.name] = cookie.value
    # print(cookies)
    url5 = response4.headers["Location"]
    # print(url5)

    return cookies, url_prefix