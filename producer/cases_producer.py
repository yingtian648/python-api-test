#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/18 10:59
# Author : LiuShiHua
# Desc : 测试用例生成器
import os
import json

from util.file_util import change_dir_to_case, get_case_jsonfile_name


class CaseProducer():
    def __init__(self):
        self.case_dir = 'case'  # 测试用例文件夹地址

    def make_api_test_case(self, api_module: str, api_str: str, model_json: dict):
        """
        生成测试用例
        :param api_str:
        :return:
        """
        if api_module is None or api_str is None:
            return
        self.make_api_test_case_file(api_module, api_str, model_json)

    def make_api_test_case_file(self, api_parent: str, api_str: str, model_json: dict):
        """
        生成测试用例 文件
        :param api_parent: 模块名 → 生成对应的文件件
        :param api_str: 接口名 → 生产对应的json文件 → 写入测试用例的基础格式语句
        :return:
        """
        if api_str is None:
            return None
        file_name = get_case_jsonfile_name(api_str)
        file_create = self.create_file(api_parent, file_name)
        if file_create:
            self.make_api_test_case_json(api_parent, api_str, file_name, model=model_json)
            return file_name
        return None

    def create_file(self, parent_dir: str, file_name: str):
        """
        创建文件
        :param file_name:
        :return:
        """
        try:
            change_dir_to_case()
            if not os.path.exists(parent_dir):  # 判断当前目录下是否存在该文件夹
                os.mkdir(parent_dir)  # 在case目录下创建parent_dir文件夹
            else:
                if not os.path.isdir(parent_dir):  # 存在该文件，但是非文件夹，删除
                    os.remove(parent_dir)
                    os.mkdir(parent_dir)  # 在case目录下创建parent_dir文件夹
            os.chdir(parent_dir)  # 进入文件夹
            if os.path.exists(file_name):  # 已存在同名文件 则不去创建
                print("已存在" + file_name)
                return False
            else:
                file = open(file_name, "w", encoding='utf-8', errors='ignore')  # 已“写入”的方式打开文件[文件不存在时会创建文件]
                file.close()
        except Exception as ec:
            print("producer创建文件失败：" + ec)
            return False
        return True

    def make_api_test_case_json(self, api_parent: str, api_str: str, file_name: str, model: dict):
        """
        生成测试用例 基础 json
        :param api_str:
        :param file_name:
        :param model:
        :return:
        """
        if model is None or api_str is None or file_name is None:
            return False
        model['url'] = "/" + api_parent + api_str
        try:
            file = open(file_name, "w", encoding='utf-8', errors='ignore')  # 已“写入”的方式打开文件[文件不存在时会创建文件]
            file.write(json.dumps(model, indent=2))
            file.close()
            return True
        except Exception as ep:
            print("producer写入文件失败：" + ep)
            return False
