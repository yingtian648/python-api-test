#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/20 15:08
# Author : LiuShiHua
# Desc :
from producer.cases_producer import CaseProducer


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


def build_test_case(case_apis: dict,model_:dict):
    """
    生产测试用例文件 放置于case目录下
    :param case_apis:
    :param model_: json模型
    :return:
    """
    try:
        if case_apis is not None and case_apis.keys() is not None:
            analysis_apis(case_apis, model_)  # 生产测试用例文件
            print("测试用例文件生产: 已完成")
    except Exception as ep:
        import traceback
        print("case_apis Exception:" + str(traceback.format_exc()))