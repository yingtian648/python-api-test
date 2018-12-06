#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/30 9:32
# Author : LiuShiHua
# Desc :
from req_util.base_request import get_api, post_api
from manifest import case_files
from req_util.log_util import log
import datetime
import time


# 从注册文件中读取测试用例文件
def find_case_to_test(base_url, base_header, base_method):
    if case_files == None or not isinstance(case_files, list) or len(case_files) == 0:
        log("\n****************** 未发现需要测试的文件 ******************\n")
        return
    log(str(datetime.datetime.now()))
    log("--------- 测试开始 --------- ")
    t1 = time.time()
    for api_case in case_files:
        log("****************** " + api_case + " ******************\n")
        try:
            file = open(api_case, "r", encoding='utf-8', errors='ignore')
        except Exception as ex:
            log("manifest错误：" + str(ex))
            continue
        content = file.read()
        try:
            content = eval(content)
        except Exception as exj:
            log("json格式错误：" + str(exj))
            continue
        make_test_detail(content, base_url, base_header, base_method)
    t2 = time.time()
    log("\n--------- 测试完成 总耗时:" + str(t2 - t1) + "毫秒 ---------")


# 构造测试
def make_test_detail(case_info: dict, base_url, base_header, base_method):
    if not case_info or 'url' not in case_info.keys() \
            or not case_info['url'] \
            or "cases" not in case_info.keys() \
            or not isinstance(case_info['cases'], list) \
            or len(case_info['cases']) == 0:
        log("退出：接口地址或测试用例错误、测试用例不存在")
        return
    if case_info['url'].startswith("http://") or case_info['url'].startswith("https://"):
        url = case_info['url']
    else:
        url = base_url + case_info['url']
    # 将文件中header添加到base_header中
    if "header" in case_info.keys() and case_info['header'] != None:
        base_header.update(case_info['header'])
    if "method" in case_info.keys() and case_info['method'] != None:
        base_method = case_info['method']
    for case in case_info['cases']:
        if "method" in case.keys() and case['method'] != None:
            base_method = case['method']
        params = None
        # 获取参数
        if "params" in case.keys() and case['params'] != None:
            params = case['params']
        # 单个用例重复测试次数
        if ("repeat" in case.keys()) and (str(case['repeat']) != None) and \
                str(case['repeat']).isdigit() and \
                case['repeat'] > 0:
            for i in range(case['repeat']):
                req_api(url, base_method, base_header, params)
        else:
            req_api(url, base_method, base_header, params)


# 请求接口
def req_api(url, method: str, header, params):
    if method.upper() == "POST":
        post_api(url=url, params=params, header=header, post_body=params)
    if method.upper() == "GET":
        get_api(url=url, params=params, header=header)
