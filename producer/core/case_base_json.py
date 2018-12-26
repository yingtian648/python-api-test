#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/18 10:59
# Author : LiuShiHua
# Desc : 测试用例默认生成的json格式

# 用于：常规GET
model_normal_get = {
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
model_header_get = {
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
model_method_get = {
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
model_performance_get = {
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

# 用于：常规POST 参数是map
model_normal_post = {
    "url": None,
    "header": {

    },
    "method": "POST",
    "cases": [
        {
            "params": {
                "key": "value"
            }
        }
    ]
}

# 用于：常规POST 参数是json
model_normal_post_json = {
    "url": None,
    "header": {
        "Content-Type": "application/json"
    },
    "method": "POST",
    "cases": [
        {
            "params": {
                "key": "value"
            }
        }
    ]
}

# 用于：[ header测试 ]用不同header去请求接口
model_header_post = {
    "url": None,
    "header": {

    },
    "method": "POST",
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
model_method_post = {
    "url": None,
    "header": {

    },
    "method": "POST",
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
model_performance_post = {
    "url": None,
    "header": {

    },
    "method": "POST",
    "cases": [
        {
            "repeat": 10,
            "params": {
                "key": "value"
            }
        }
    ]
}
