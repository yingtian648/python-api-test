### 用途
1.自动化测试接口
### 核心
1.发送请求的核心文件：base_request.py<br>
2.自动生成测试用例文件：详见producer文件夹中文件<br>
### 思想
1.将请求核心、配置核心、执行核心，用例文件分离，方便使用者完成多种配置方式去执行测试用例<br>
2.一键生成测试用例文件<br>
3.一键执行测试<br>
### 说明
1.这里的POST请求，默认了2中发送数据的方式：json字符串，map参数<br>
2.这里的GET请求，拼接的请求参数<br>
### 配置
1.producer/api_list.py  ——  测试用例按模块将模块中的api名称写入对应的模块list中【自动生成测试用例时使用】<br>
2.manifest.py  ——  测试用例注册文件【所有测试用例文件路径注册到这里】 —— 是运行时首先会根据此文件去查询测试用例，再去循环执行测试用例<br>
3.case —— 测试用例文件根目录【所有测试用例文件[json文件]放置在这里】<br>
4.用例json文件[详见以下“测试用例文件”]<br>
5.main.py —— 执行测试的入口文件，这里可以配置请求的“BASE_URL == 接口地址”“BASE_HEADER == 请求头”“BASE_METHOD == 请求方法GET\POST”【需要将BASE_URL改成自己需要测试的接口地址】,“SUCCESS_CODE == 请求接口后判断是否请求成功的code”<br>
6.test_log.txt —— 测试过程中的日志会写入此文件<br>
### 运行
1.运行producer/builder.py  自动生成对应的模块测试用例文件【可自行配置初始化json模型】【生成的目录信息从case_form复制到manifest中的api_files中即可】<br>
2.运行main.py  开始测试<br>
### 附:测试用例文件，详见case/base中的_testCase.json文件
1.url[str] 如果测试用例中url以“http://”或“https://”开头，这在执行用例时则不会去拼接main.py中的BASE_URL,不含有，则会拼接在main.py中的BASE_URL的后面去请求<br>
2.header[dict] 如果测试用例/单个测试用例中有header会以字典的update方式合并到main.py中的BASE_HEADER里面【header包含"Content-Type": "application/json"则默认POST请求参数是json字符串，
以json字符串的方式去请求，否则默认POST方式请求参数是map】【单个测试用例中的header >> 测试用例最外层header >> main.py中的BASE_HEADER】<br>
3.cases[list] 是测试用例列表<br>
4.method[str] 是请求方法，如果cases中有method,则执行此method，否则执行最外层的method,最外层也没有method，则去以“GET”方式请求接口<br>
5.automationCase[dict] 自动化交叉测试用例【暂未实现】<br>
6.repeat[int] 测试用例重复测试次数<br>
以下是一个完整的测试用例<br>
```
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
      "header": {"token":"SAHDJASHDAHSQUWUISDJASJDAJ=="},
      "method": "POST",
      "repeat": 10,
      "params": {
        "evId": "197363018554679296",
        "fileNumber": "1111"
      }
    }
  ]
}
```
