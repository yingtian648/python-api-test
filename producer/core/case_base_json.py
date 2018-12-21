#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/18 10:59
# Author : LiuShiHua
# Desc : 测试用例默认生成的json格式

# 用于：常规
model_normal = {
    "url": None,
    "header": {

    },
    "method": "GET",
    "cases": [
        {
            "params": {
                "key": "value"
            }
        }
    ]
}

# 用于：[ header测试 ]用不同header去请求接口
model_header = {
    "url": None,
    "header": {

    },
    "method": "GET",
    "cases": [
        {
            "header": {

            },
            "params": {
                "key": "value"
            }
        }
    ]
}

# 用于：[ GET/POST测试 ]使用相同的用例重复请求接口 repeat:重复请求次数，默认重复10次
model_method = {
    "url": None,
    "header": {

    },
    "method": "GET",
    "cases": [
        {
            "method": "GET",
            "params": {
                "key": "value"
            }
        },
        {
            "method": "POST",
            "params": {
                "key": "value"
            }
        }
    ]
}

# 用于：[ 性能测试 ]使用相同的用例重复请求接口 repeat:重复请求次数，默认重复10次
model_performance = {
    "url": None,
    "header": {

    },
    "method": "GET",
    "cases": [
        {
            "repeat": 10,
            "params": {
                "key": "value"
            }
        }
    ]
}
