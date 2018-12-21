#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/20 15:18
# Author : LiuShiHua
# Desc :
import datetime
import time


# 从注册文件中读取测试用例文件
from manifest import case_files
from req_base.api_option import make_test_detail
from util.log_util import log


def find_case_file_to_test(base_url: str, base_header: dict, base_method: str):
    """
    单个测试文件校验并测试
    :param base_url:
    :param base_header:
    :param base_method:
    :return:
    """
    if case_files is None or not isinstance(case_files, list) or len(case_files) == 0:
        log("\n****************** 未发现需要测试的文件 ******************\n")
        return
    log(str(datetime.datetime.now()))
    log("--------- 测试开始 --------- ")
    for api_case in case_files:
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
