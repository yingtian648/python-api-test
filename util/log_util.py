#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/27 17:23
# Author : LiuShiHua
# Desc :

from util.file_util import change_dir_to_case
import os


# 打印日志 输出到文档
def log(msg: str, parent_dir=None):
    if msg is None:
        return
    print(msg)
    write_into_file(msg)


# 写入文档
def write_into_file(msg: str, parent_dir=None):
    if parent_dir is None:
        file = open("test_log.txt", "a", encoding='utf-8', errors='ignore')
        file.write(msg + "\n")
        file.close()
    else:
        change_dir_to_case()
        os.chdir(parent_dir)
        file = open("test_log.txt", "a", encoding='utf-8', errors='ignore')
        file.write(msg + "\n")
        file.close()
        change_dir_to_case()
