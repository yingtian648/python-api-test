#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/20 15:08
# Author : LiuShiHua
# Desc :
from producer.core.cases_producer import CaseProducer
from util.file_util import get_case_jsonfile_name


def analysis_apis(case_apis: dict, model: dict):
    """
    分析manifest  → 生产测试用例文件
    :param case_apis:
    :param model:
    :return:
    """
    pud = CaseProducer()
    for key in case_apis.keys():
        if case_apis[key] is not None and isinstance(case_apis[key], list) and len(case_apis[key]) > 0:
            for api_case in case_apis[key]:
                pud.make_api_test_case(key, api_case, model)


def build_test_case(case_apis: dict, model_: dict):
    """
    生产测试用例文件 放置于case目录下
    :param case_apis:
    :param model_: json模型
    :return:
    """
    try:
        if case_apis is not None and case_apis.keys() is not None:
            build_dir_to_case_form(case_apis)
            analysis_apis(case_apis, model_)  # 生产测试用例文件
            print("测试用例文件生产: 已完成")
    except Exception as ep:
        import traceback
        print("case_apis Exception:" + str(traceback.format_exc()))


BASE_CASE_FORM = './case_form.txt'


def build_dir_to_case_form(case_apis: dict):
    """
    将一键生成的测试用例文件的目录信息写入case_form
    :param case_apis:
    :return:
    """
    for key in case_apis.keys():
        cases = case_apis[key]
        if cases is not None and isinstance(cases, list) and len(cases) > 0:
            for case in cases:
                file_name = get_case_jsonfile_name(case)
                file = open(BASE_CASE_FORM, "a", encoding='utf-8', errors='ignore')  # 已“写入”的方式打开文件[文件不存在时会创建文件]
                file.write('\"./case/' + key + '/' + file_name + '\",\n')
                file.close()
