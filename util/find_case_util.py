#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/20 15:18
# Author : LiuShiHua
# Desc :
import datetime
import time

from manifest import case_apis
from req_base.api_option import check_case_file_to_test
from util.file_util import change_dir_to_case


def find_case_to_test(base_url, base_header, base_method):
    try:
        if case_apis is not None and case_apis.keys() is not None:
            for key in case_apis.keys():
                if case_apis[key] is not None and isinstance(case_apis[key], list) and len(case_apis[key]) > 0:
                    for api_case_str in case_apis[key]:
                        print(api_case_str)
                        change_dir_to_case()
                        check_case_file_to_test(key, api_case_str, base_url, base_header, base_method)

    except Exception as ep:
        import traceback
        print("case_apis Exception:" + str(traceback.format_exc()))
