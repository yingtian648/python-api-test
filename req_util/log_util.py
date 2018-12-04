#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/11/27 17:23
# Author : LiuShiHua
# Desc :

# 打印日志 输出到文档
def log(msg: str):
    print(msg)
    write_into_file(msg)

# 写入文档
def write_into_file(msg):
    file = open("test_log.txt", "a", encoding='utf-8', errors='ignore')
    file.write(msg + "\n")
    file.close()
