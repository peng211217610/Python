#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''走pytest流程的情况'''

# 引入包
from Function.Config.env_variable import *
from Function.Page.function_page_BasePage import *

#获取全局的默认账号的session
password = '123'
# session = manager.get_session(username,password)        #这里后续要打开



#获取截图和日志
# ================= 全局变量 =================
pytest_img_dir = "artifacts/Images"
md_file_path = "artifacts/report.md"
pytest_log_file = "artifacts/run.log"


#获取截图
def capture_and_record_image(case_name, driver=None, switch='N'):
    """截图并追加 Markdown 记录（仅当传入 driver 且开关为 Y 时执行）"""
    if str(switch).upper() != 'Y' or driver is None:
        return
    safe_case_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in case_name)
    img_name = f"{safe_case_name}_{mytime}.png"
    img_abs_path = os.path.join(pytest_img_dir, img_name)
    try:
        driver.save_screenshot(img_abs_path)
        print(f"[截图已保存] {img_abs_path}")
    except Exception as e:
        print(f"[截图失败] {e}")
        return
    md_line = f"![1094](../Images/{mytime}.png)\n"
    with open(md_file_path, 'a', encoding='utf-8') as f:
        f.write(md_line)
    print(f"[Markdown记录已更新] {md_file_path}")

#获取日志
def record_case_log(log_msg, case_name, status, switch='N'):
    """纯文本日志记录（开关为 Y 时执行）"""
    if str(switch).upper() != 'Y':
        return
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = (
        f"[{current_time}] 用例: {case_name} | 状态: {status}\n"
        f"详细信息: {log_msg}\n"
        f"{'-' * 60}\n"
    )
    with open(pytest_log_file, 'a', encoding='utf-8') as f:
        f.write(log_content)
    print(f"[日志已记录] {pytest_log_file}")










if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
