#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''基础配置'''

# 引入包
import os,sys,shutil,json,copy,os.path,ctypes,io
from pathlib import Path





#常用文件夹地址
# python_dir=get_python_dir()
# python_dir=r'D:\TDdownload\BaiduSyncdisk\Document\Python'
python_dir = str(Path(__file__).resolve().parent.parent.parent)
Document_dir=os.path.dirname(python_dir)
td_dir=os.path.dirname(Document_dir)
download_dir=os.path.join(td_dir,'下载')
testfile_dir=os.path.join(Document_dir,'TestFile')
file_dir=os.path.join(python_dir,'File')
csv_dir=os.path.join(file_dir,'CSV')
excel_dir=os.path.join(file_dir,'Excel')
txt_dir=os.path.join(file_dir,'TXT')
json_dir=os.path.join(file_dir,'JSON')
log_dir=os.path.join(file_dir,'LOG')
img_dir=os.path.join(file_dir,'IMG')
ultra_dir=os.path.join(file_dir,'UltraEdit')
tool_dir=os.path.join(python_dir,'Tools')
django_dir=os.path.join(python_dir,'Django')
secguard_dir=os.path.join(td_dir,'下载','安全扫描')
excel_config=os.path.join(excel_dir,'000_我的配置.xls')
stock_config=os.path.join(excel_dir,'My Stock.xls')
touzi_json=os.path.join(json_dir,'投资.json')
knowledge_dir=os.path.join(python_dir,'知识')
data_dir=os.path.join(python_dir,'知识','数据')
config_dir=os.path.join(python_dir,'Function','Config')
whether_update_high_low_config=os.path.join(txt_dir,'update_high_low.txt')
no_need_sync_dir=os.path.join(python_dir,'无需同步')
temp_txt=os.path.join(python_dir,'无需同步','temp_txt.txt')
sto_csv=os.path.join(python_dir,'无需同步','股票操作.csv')
stock_data_dir=os.path.join(knowledge_dir,'股票数据','股票分时数据')
caogao1_txt=os.path.join(ultra_dir,'草稿1.txt')
caogao2_txt=os.path.join(ultra_dir,'草稿2.txt')
sqlite_db=os.path.join(data_dir,'sqlite_db')
lightshot_dir=os.path.join(python_dir,'LightShot')
ziliao_dir=os.path.join(python_dir,'资料')
TestResult_dir=os.path.join(python_dir,'TestCase','TestResult')






















if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
