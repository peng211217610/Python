# Python

主代码在Function下

Function/Config/basic_variable.py，这里对经常使用的路径配置成变量

Function/Common/function_common.py是我的基础函数或类，对一些常用到的功能做了封装

Function/Config/common_variable.py，这里是一些基础的变量

Function/Oppty/function_oppty_database.py，这里将数据库的操作封装，测试过程中经常要查数据库

Function/Oppty/function_oppty_api_login.py，是接口请求的封装

Function/Oppty/function_oppty_common.py，一些初始化的操作，比如生成一个不会重复的数字，生成测试用的文件或者压缩包等，给后续的测试用例用

Function/Common/function_init_webdriver.py，UI自动化的初始化操作，主要就是定义driver

Function/Common/function_init_appiumdriver.py，移动端UI自动化的初始化操作，跟Web端从这里分离

Function/Page/function_page_BasePage.py，Web自动化的基础封装，主要是封装查找元素、点击等方法

Function/Oppty/function_pytest_common.py，使用pytest组装用例，统一以此为入口

Python/TestCase/HW就是测试脚本所在的路径，划分api和ui，conftest里配置前置和后置操作，pytest.ini我没上传到仓库来，需要自己配置，其他例如Report，截图，日志等文件夹或文件没有上传上来。因为涉及具体项目，不方便上传。

Python/知识/知识汇总是我的学习笔记，这个才是我要表达的重点。其中又以Web UI自动化，MySQL查询，Locust性能，数据结构与算法为重点。
