#【核心】
1.发送请求的核心文件：base_request.py<br>
#【思想】
将请求核心、配置核心、执行核心，用例文件分离，方便使用者完成多种配置方式去执行测试用例<br>
#【说明】
1.这里的POST请求，默认了2中发送数据的方式：json字符串，map参数<br>
2.这里的GET请求，拼接的请求参数<br>
#【配置】
1.manifest.py  ——  测试用例注册文件【所有测试用例文件路径注册到这里】 —— 是运行时首先会根据此文件去查询测试用例，再去循环执行测试用例<br>
2.case —— 测试用例文件根目录【所有测试用例文件[json文件]放置在这里】<br>
3.用例json文件[详见以下“测试用例文件”]<br>
4.main.py —— 执行测试的入口文件，这里可以配置请求的“接口地址”“header”“请求方法GET\POST”【需要将BASE_URL改成自己需要测试的接口地址】<br>
5.test_log.txt —— 测试过程中的日志会写入此文件<br>
#【运行】
1.运行main.py<br>
#【测试用例文件，详见case/test_dir中的demo.json文件】
1.url 如果测试用例中url以“http://”或“https://”开头，这在执行用例时则不会去拼接main.py中的BASE_URL,不含有，则会拼接在main.py中的BASE_URL的后面去请求<br>
2.header 如果测试用例中有header会以字典的update方式合并到main.py中的BASE_HEADER里面【header包含"Content-Type": "application/json"则默认POST请求参数是json字符串，
以json字符串的方式去请求，否则默认POST方式请求参数是map】<br>
3.cases 是测试用例列表<br>
4.method 是请求方法，如果cases中有method,则执行此method，否则执行最外层的method,最外层也没有method，则去以“GET”方式请求接口<br>
5.automationCase 自动化交叉测试用例【暂未实现】<br>
以下是一个完整的测试用例<br>
{
  "url": "/signIn/getSignIn",
  "header": {
    "Authorization": "MTc2OF90b2tlbl8xNTQzNDgxNjk1OTY2LCwsMTU0MzQ4MTY5NTk2Ng==",
    "Content-Type": "application/json"
  },
  "method": "POST",
  "automationCase": {
    "header":{},
    "method":{},
    "params":{
      "evId":["197363018554679296","1212",1112],
      "fileNumber":["11111",22222]
    }
  },
  "cases": [
    {
      "method": "POST",
      "params": {
        "evId": "197363018554679296",
        "fileNumber": "1111"
      }
    }
  ]
}
