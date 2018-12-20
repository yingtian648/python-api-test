#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/20 15:27
# Author : LiuShiHua
# Desc :

def get_case_jsonfile_name(api_str: str):
    """
    根据api路径生成json文件名
    :param api_str:
    :return:
    """
    file_name = None
    if "/" in api_str:
        for ns in api_str.split('/'):
            if file_name is None:
                file_name = ns
            else:
                file_name = file_name + "_" + ns
    else:
        file_name = api_str
    return file_name + ".json"


BASE_CASE_DIR = 'case'


def change_dir_to_case():
    import os
    """
    如果当前目录是case目录的父目录，则进入case目录
    如果不是，则递归方式返回上一级目录
    【这里不考虑其他不相关路径 和 处于父级路径的情况】
    :return:
    """
    dirs = os.getcwd().split('\\')
    if BASE_CASE_DIR in dirs:
        str_nd = dirs[len(dirs) - 1]
        if BASE_CASE_DIR == str_nd:
            return
    if os.path.exists(BASE_CASE_DIR):
        os.chdir(BASE_CASE_DIR)
    else:
        os.chdir(r'../')
        change_dir_to_case()
