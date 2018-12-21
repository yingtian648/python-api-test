#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/21 9:31
# Author : LiuShiHua
# Desc : 测试用例生成器 —— 执行后生成对应的测试用例
from producer.api_list import test_case_list, base_test_list
from producer.core.case_base_json import *
from producer.core.analysis_util import build_test_case

# case_apis是测试和生成测试用例的基础
# "test_case" 键：建议使用模块名
#      键 【最后生成的json文件url =  test_case + /elevator/getEvList】
# "test_case_list" 值：模块对应的接口列表
case_apis = {
    "test-case": test_case_list,
    "base": base_test_list,
}

if __name__ == '__main__':
    build_test_case(case_apis, model_normal)  # model_normal是生成测试用例json文件的基础格式标准[可自行定义]