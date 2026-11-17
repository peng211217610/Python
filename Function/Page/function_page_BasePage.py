#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''BasePage类'''

# 引入包
from Function.Common.function_init_webdriver import *



#解析Markdown文件，获取参数，给parametrize用
#有问题：set('') 是空集，issubset({'-',':'}) 恒真 → 任何含空单元格的行都会被当成"分割线"跳过
#导入期解析 md；建议改惰性加载 + 缓存
def get_param_from_markdown(md_file):
    """
    自定义解析 Markdown 文件，生成目标嵌套字典格式：
    {
        "一级标题": {
            "二级标题A": {
                "三级标题A1": [ {"字段1": "值1", "字段2": "值2"}, ... ],
                "三级标题A2": [ ... ]
            },
            "二级标题B": { ... }
        }
    }
    所有值保留为字符串，剔除 expect_ 开头的空字段。
    """
    if not os.path.exists(md_file):
        raise FileNotFoundError(f"找不到 Markdown 文件: {md_file}")

    result = {}

    current_h1 = None
    current_h2 = None
    current_h3 = None
    headers = []

    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        # 遇到空行，重置表头状态，防止表格数据串行
        if not line:
            headers = []
            continue

        # 1. 识别一级标题 (#)
        if line.startswith("# "):
            current_h1 = line[2:].strip()
            result[current_h1] = {}  # 一级标题的值是字典
            current_h2 = None
            current_h3 = None
            headers = []
            continue

        # 2. 识别二级标题 (##)
        if line.startswith("## "):
            current_h2 = line[3:].strip()
            current_h3 = None
            if current_h1:
                # 二级标题作为一级标题字典的键，其值也是字典
                result[current_h1][current_h2] = {}
            headers = []
            continue

        # 3. 识别三级标题 (###)
        if line.startswith("### "):
            current_h3 = line[4:].strip()
            if current_h1 and current_h2:
                # 三级标题作为二级标题字典的键，其值是列表
                result[current_h1][current_h2][current_h3] = []
            headers = []
            continue

        # 4. 识别表格数据 (以 | 开头)
        if line.startswith("|"):
            # 如果不在三级标题下，直接忽略
            if not (current_h1 and current_h2 and current_h3):
                continue

            cells = [c.strip() for c in line.strip("|").split("|")]

            # 处理表头
            if not headers:
                headers = cells
                continue

            # 跳过 Markdown 分割线行 (如 |---|---|)
            if all(set(c).issubset({'-', ':'}) for c in cells):
                continue

            # 处理数据行
            row_dict = {}
            for i, header in enumerate(headers):
                value = cells[i] if i < len(cells) else ""

                # 过滤逻辑：expect_开头的键，且值为空，则舍弃
                if header.startswith("expect_") and value == "":
                    continue

                # remark 键的空值：赋值为 None
                if header == "remark" and not value:
                    row_dict[header] = None
                    continue

                # 一律保留字符串
                row_dict[header] = value

            # 将数据字典加入对应三级标题的列表中
            if row_dict:
                result[current_h1][current_h2][current_h3].append(row_dict)

    return result

#获取参数字典
md_file = os.path.join(python_dir,'TestCase','TestResult','测试参数.md')
param_dict = get_param_from_markdown(md_file)

#把param_dict传给本函数，返回三级标题对应的列表
def _find_data_by_h3(md_data, target_h3):
    """
    内部递归函数：在嵌套字典中查找指定的三级标题，返回其对应的列表。
    """
    def _search(data):
        if isinstance(data, dict):
            # 如果当前字典中有这个三级标题，直接返回对应的列表
            if target_h3 in data:
                return data[target_h3]
            # 否则遍历所有的值，继续往下找
            for value in data.values():
                result = _search(value)
                if result is not None:
                    return result
        return None

    data = _search(md_data)
    if data is None:
        raise ValueError(f"在数据中未找到三级标题: [{target_h3}]")
    return data


#对列表进行过滤，如果包含only_run这个参数，就只运行勾选了的部分。没有参数或没有标记，就是全量执行
def _apply_filter(test_data):
    """
    根据 only_run 标记过滤数据。
    规则：
    1. 如果没有任何行有 only_run 标记，返回所有数据。
    2. 如果有标记（一行或多行），只返回被标记的行。
    """
    if not test_data:
        return test_data

    # 筛选出带有有效标记的行（不区分大小写，支持 1/y/yes/true/是）
    marked_data = [
        row for row in test_data
        if str(row.get("only_run", "")).strip().lower() in ("1", "y", "yes", "true", "是")
    ]

    # 如果有被标记的行（无论是一条还是多条），就只返回这些标记的行
    if marked_data:
        return marked_data

    # 如果没有任何标记，返回全部数据
    return test_data




#获取test_data，也就是parametrize利的argvalues
def get_test_data(item,md_data=None):
    """
    获取 test_data。
    """
    if md_data is None:
        md_data = param_dict
    raw_data = _find_data_by_h3(md_data, item)
    return _apply_filter(raw_data)


#获取case_id，就是parametrize利的ids
def get_case_ids(item,md_data=None):
    """
    获取 case_ids。
    同样根据传入的 md_data 和 target_h3 查找到字典列表，
    然后提取其中的 remark 作为 ids（如果为空则返回 None）。
    """
    if md_data is None:
        md_data = param_dict
    raw_data = _find_data_by_h3(md_data,item)
    filtered_data = _apply_filter(raw_data)
    if not isinstance(filtered_data, list):
        return []
    # 提取 remark，如果为空（或 None）则用 or None 兜底
    return [case.get("remark") or None for case in filtered_data]

#使用的时候，只要传get_test_data('test_001'),ids=get_case_ids('test_001')

















#自定义基础工具类
class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.handle = driver.handle

    #元素定位
    def find(self,loc):
        return self.driver.find_element(*loc)

    #元素定位-显式等待
    def fd_element(self,loc,timeout=10):
        """元素定位的公共方法"""
        try:
            element = WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(loc))
        except Exception as e:
            print('这里是错误日志')
            raise
        return element

    #显式等待
    def find_element_use_webdriverwait(self):
        pass

    #div/ul/li格式的滚动条，让隐藏元素进入可视区域
    def ele_scrollIntoView(self,ele):
        """ele是被隐藏的元素"""
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center', inline:'nearest'});", ele)


    #Select选择框的封装
    #Select 类只适用于 HTML 原生的 <select> 标签（即 <select><option>...</option></select>）
    #如果下拉框在页面底部，有时不滚动到可见区域，Select 会报错 ElementNotInteractableException
    def base_select(self,loc,text):
        Select(self.driver.find_element(*loc)).select_by_visible_text(text)

    #点击
    def click(self,loc):
        #显式等待元素可点击，然后点击
        pass

    #输入文本
    def send_keys(self,loc,text):
        ele = self.find(loc)
        ele.clear()
        ele.send_keys(text)





























if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
