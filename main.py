#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/29 14:16
# Author : LiuShiHua
# Desc :


# 默认测试地址
from util.find_case_util import find_case_file_to_test

BASE_URL = 'http://172.16.2.74:8080'
# 默认请求方法
BASE_METHOD = "GET"
# 默认请求成功后返回code
SUCCESS_CODE = 0

# "Content-Type": "application/json"
BASE_HEADER = {
    "Authorization": "MjE5OTIwMzA4Mjk4MDk2NjQwX3Rva2VuXywsLDE1NDU2MTYwMTkzNjM=",
}

if __name__ == '__main__':
    find_case_file_to_test(BASE_URL, BASE_HEADER, BASE_METHOD)
