#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/29 14:16
# Author : LiuShiHua
# Desc :
from req_util.api_option import find_case_to_test

# 默认测试地址
BASE_URL = 'http://172.16.2.74:8080'
# BASE_URL = 'http://api.t4.2012iot.com'
# 默认请求方法
BASE_METHOD = "GET"

# "Content-Type": "application/json"
BASE_HEADER = {
    "Authorization": "MTc2OF90b2tlbl8xNTQzMzk4NzEzMDUyLCwsMTU0MzM5ODcxMzA1Mg==",
    "tokenStr": "MTc2OF90b2tlbl8xNTQzMjg1MjAyMDU3LCwsMTU0MzI4NTIwMjA1Nw==",
}

if __name__ == '__main__':
    find_case_to_test(BASE_URL,BASE_HEADER,BASE_METHOD)
