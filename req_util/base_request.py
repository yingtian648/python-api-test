#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/27 14:31
# Author : LiuShiHua
# Desc :
from urllib.request import Request, urlopen
from urllib.parse import quote, urlencode
import json
from req_util.log_util import log

success_code = 0  # 请求成功的返回code


def post_api(url, params: dict, header: dict, post_body: dict):
    """
    尝试POST方式请求接口
    :param url:
    :param params:
    :param header:
    :param post_body:
    :return:
    """
    if header and "Content-Type" in header.keys() and header['Content-Type'] == 'application/json':  # 请求参数是json
        req = Request(url=url, data=json.dumps(post_body).encode('utf-8'), headers=header, method='POST')
    else:  # 请求参数是map
        params = urlencode(params).encode('utf-8')  # 编码请求参数
        req = Request(url=url, data=params, headers=header, method='POST')
    process_result(url, req, params, header, "POST")


def get_api(url, params: dict, header: dict):
    """
    尝试GET方式请求接口
    :param url:
    :param params: quote(params[key], safe='/', encoding='utf-8', errors=None) 防止中文编码错误问题
    :param header:
    :return:
    """
    get_params = None
    if params:
        for key in params.keys():
            if params[key]:
                if not get_params:
                    get_params = "?" + quote(key, safe='/', encoding='utf-8', errors=None) + "=" + quote(params[key],
                                                                                                         safe='/',
                                                                                                         encoding='utf-8',
                                                                                                         errors=None)
                else:
                    get_params += "&" + quote(key, safe='/', encoding='utf-8', errors=None) + "=" + quote(params[key],
                                                                                                          safe='/',
                                                                                                          encoding='utf-8',
                                                                                                          errors=None)
    if get_params:
        url += get_params
    if header:
        req = Request(url=url, headers=header, method='GET')
    else:
        req = Request(url=url, method='GET')
    process_result(url, req, params, header, "GET")


def process_result(url, req, params, header, methodStr):
    """
    处理请求返回结果
    :param req:
    :return:
    """
    result_content = None
    try:
        result_content = urlopen(req).read().decode('utf-8')
        result_content = json.loads(result_content)
        if result_content['code'] and not result_content['code'] == success_code:
            log('------操作失败------')
            log('request_url:' + url)
            log('request_method:' + methodStr)
            log('request_header:' + str(header))
            log('request_params:' + str(params))
            log('response:' + str(result_content))
        else:
            log('------操作成功------')
            log(str(result_content))

    except Exception as excp:
        log('------请求异常------')
        log('request_url:' + url)
        log('request_method:' + methodStr)
        log('request_header:' + str(header))
        log('request_params:' + str(params))
        log('response:' + str(result_content))
        log('error:' + str(excp))
