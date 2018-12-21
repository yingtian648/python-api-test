#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/30 9:32
# Author : LiuShiHua
# Desc :
from manifest import case_files
from req_base.base_request import get_api, post_api
from util.log_util import log

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
    log("\n****************** START " + url + " ******************\n")
    # 将文件中header更新到base_header中
    if "header" in case_info.keys() and case_info['header'] is not None:
        base_header.update(case_info['header'])
    if "method" in case_info.keys() and case_info['method'] is not None:
        base_method = case_info['method']
    average_total_time = 0  # 单个请求消耗时长累计值
    req_times = 0  # 单个有效请求次数
    req_times_error = 0  # 单个无效请求次数
    for case in case_info['cases']:
        if "method" in case.keys() and case['method'] is not None:
            base_method = case['method']
        params = None
        # 获取参数
        if "params" in case.keys() and case['params'] is not None:
            params = case['params']
        # 将单个用例中的header更新到base_header中
        if "header" in case.keys() and case['header'] is not None:
            base_header.update(case['header'])
        # 单个用例重复测试次数
        if ("repeat" in case.keys()) and (str(case['repeat']) is not None) and \
                isinstance(case['repeat'], int) and \
                case['repeat'] > 0:
            for i in range(case['repeat']):
                user_time = req_api(url, base_method, base_header, params)
                if user_time != -1:
                    average_total_time = average_total_time + user_time
                    req_times = req_times + 1
                else:
                    req_times_error = req_times_error + 1
        else:
            user_time_1 = req_api(url, base_method, base_header, params)
            if user_time_1 != -1:
                average_total_time = average_total_time + user_time_1
                req_times = req_times + 1
            else:
                req_times_error = req_times_error + 1
    average_t = 0
    if req_times > 0:
        average_t = round((average_total_time / req_times), 8)
    log("\n****************** END 总耗时:" + str(round(average_total_time, 8)) + " 平均请求时长:" + str(
        average_t) + "毫秒 有效请求" + str(req_times) + "次 无效请求" + str(req_times_error) + "次 ******************")


# 请求接口
def req_api(url, method: str, header, params):
    if method.upper() == "POST":
        return post_api(url=url, params=params, header=header, post_body=params)
    elif method.upper() == "GET":
        return get_api(url=url, params=params, header=header)
    else:
        log("请求方法method非GET/POST")
        return -1
