#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/29 14:16
# Author : LiuShiHua
# Desc :
from req_util.api_option import find_case_to_test

# 默认测试地址
BASE_URL = 'http://172.16.2.74:8080'
# 默认请求方法
BASE_METHOD = "GET"
# 默认请求成功后返回code
SUCCESS_CODE = 0

# "Content-Type": "application/json"
BASE_HEADER = {
    "Authorization": "MTc2OF90b2tlbl8xNTQ0MDY0Mzc5MDI0LCwsMTU0NDA2NDM3OTAyNA==",
}

if __name__ == '__main__':
    find_case_to_test(BASE_URL, BASE_HEADER, BASE_METHOD)
