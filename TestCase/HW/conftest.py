#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''conftest'''

# 引入包：所有pytest的测试文件，都走pytest_common
from Function.Oppty.function_pytest_common import *
from Function.Page.function_page_HomePage import *

#获取浏览器驱动
@pytest.fixture(scope="session",autouse=False)
def driver():
    driver = Driver.get_driver()
    # driver.get('https://www.baidu.com') #登陆首页
    #将Handle实例化后，将其赋给driver，并取名Handle，于是就成了driver本身的方法
    #而driver是BasePage里的，所以在继承BasePage类的页面脚本里，直接用self.handle.switch_to_the_latest_handle()
    #测试用例上可以使用driver.handle.switch_to_the_latest_handle()，但不推荐在测试用例里写这种代码
    driver.handle = Handle(driver)
    yield driver
    driver.quit()


#登陆首页
@pytest.fixture(scope="session")
def logged_in_driver(driver):
    print("\n[session] 首次登录，后续不再重复登录")
    LoginPage(driver).login("user_A", "pwd_A")
    return driver

#回到首页
@pytest.fixture(scope="module")
def home_page(logged_in_driver):
    """每个模块（测试文件）开始时，确保回到首页"""
    print("\n[module] 重新回到首页，准备进入当前模块")
    # 强制刷新回到首页，消除上一个模块留下的页面状态
    page = HomePage(logged_in_driver)
    page.back_to_homepage()
    return page






#这里要写一个tear_down的方法，每个用例执行完，都关闭掉主窗口之外的窗口，并切回主窗口




# 钩子：把用例每一步（setup/call/teardown）的结果，塞到 request.node 上
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

#截图和记录日志，想要截图，就在函数里传auto_record
@pytest.fixture(autouse=False)
def auto_record(request):
    yield
    # 获取用例结果和状态
    if hasattr(request.node, "rep_call"):
        outcome = request.node.rep_call.outcome
        status = "PASS" if outcome == "passed" else "FAIL"
        log_msg = str(request.node.rep_call.longrepr) if status == "FAIL" else "执行成功"
    else:
        status = "UNKNOWN"
        log_msg = ""
    case_name = request.node.name
    # 尝试获取 driver（如果是接口测试，拿不到就是 None）
    driver = getattr(request.node, "driver", None)
    # 调用截图函数（开关设为 Y，接口测试没 driver 会自动跳过）
    capture_and_record_image(
        case_name=case_name,
        driver=driver,
        switch="Y"
    )
    # 调用日志函数（开关设为 Y）
    record_case_log(
        log_msg=log_msg,
        case_name=case_name,
        status=status,
        switch="Y"
    )












#我在api_login里写了构建session池，这里就可以不要
#在测试用例中，参数里写login_as，就可以通过session_A = login_as("user_A", "pwd_A")获得一个session
#接口，登陆函数
# @pytest.fixture(scope="session")
# def login_as():
#     """这是一个工厂 fixture，它返回一个函数，用来动态创建各种账号的 session"""
#     sessions = {}  # 用字典缓存 session，防止同一个账号重复登录
#
#     def _login(username, password):
#         if username in sessions:
#             return sessions[username]
#         s = requests.Session()
#         s.post("http://api.com/login", data={"user": username, "pwd": password})
#         sessions[username] = s
#         return s
#
#     return _login  # 返回内部的函数















if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
