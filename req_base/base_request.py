#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/27 14:31
# Author : LiuShiHua
# Desc :
from urllib.request import Request, urlopen
from urllib.parse import quote, urlencode
import json, time
from util.log_util import log


def post_api(url, params: dict, header: dict, post_body: dict):
    """
    尝试POST方式请求接口
    :param url:
    :param params:
    :param header:
    :param post_body:
    :return:请求消耗时长
    """
    if header and "Content-Type" in header.keys() and header['Content-Type'] == 'application/json':  # 请求参数是json
        req = Request(url=url, data=json.dumps(post_body).encode('utf-8'), headers=header, method='POST')
    else:  # 请求参数是map
        params = urlencode(params).encode('utf-8')  # 编码请求参数
        req = Request(url=url, data=params, headers=header, method='POST')
    return process_result(url, req, params, header, "POST")


def get_api(url, params: dict, header: dict):
    """
    尝试GET方式请求接口
    :param url:
    :param params: quote(params[key], safe='/', encoding='utf-8', errors=None) 防止中文编码错误问题
    :param header:
    :return:请求消耗时长
    """
    get_params = None
    if params is not None:
        for key in params.keys():
            if params[key] is not None:
                if not get_params:
                    get_params = "?" + quote(key, safe='/', encoding='utf-8', errors=None) + "=" + quote(
                        str(params[key]),
                        safe='/',
                        encoding='utf-8',
                        errors=None)
                else:
                    get_params += "&" + quote(key, safe='/', encoding='utf-8', errors=None) + "=" + quote(
                        str(params[key]),
                        safe='/',
                        encoding='utf-8',
                        errors=None)
    if get_params is not None:
        url += get_params
    if header is not None:
        req = Request(url=url, headers=header, method='GET')
    else:
        req = Request(url=url, method='GET')
    return process_result(url, req, params, header, "GET")


def process_result(url, req, params, header, methodStr):
    from main import SUCCESS_CODE  # 请求成功的返回code
    """
    处理请求 打印结果 返回消耗时长
    :param req:
    :return:请求消耗时长
    """
    result_content = None
    tottime_long = -1
    try:
        t1 = time.time()
        result_content = urlopen(req).read().decode('utf-8')
        tottime_long = time.time() - t1
        tottime_str = ("use_time: " + str(tottime_long)) + " ms"
        result_content = json.loads(result_content)
        if result_content['code'] and not result_content['code'] == SUCCESS_CODE:
            log('------ Failure ' + url + ' ------')
            log('request_method:' + methodStr)
            log('request_header:' + str(header))
            log('request_params:' + str(params))
            log('response:' + str(result_content))
        else:
            log('------ Success ' + url + ' ' + tottime_str + ' ------')
            log(json.dumps(result_content, indent=2))  # 美化json输出

    except Exception as excp:
        log('------ Exception ' + url + ' ------')
        log('request_method:' + methodStr)
        log('request_header:' + str(header))
        log('request_params:' + str(params))
        log('response:' + str(result_content))
        log('error:' + str(excp))
    return tottime_long
