#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/29 13:58
# Author : LiuShiHua
# Desc : 注册测试用例文件

# 存放测试用例的相对地址
# producer.case_base_json 目录下有多个json格式 如需自定义可以自己去改
from api_list import *
from producer.case_base_json import *
from util.build_case_file_util import build_test_case

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
