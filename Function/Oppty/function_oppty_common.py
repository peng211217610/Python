#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

# 引入包
from Function.Config.env_variable import *
from Function.Oppty.function_oppty_api_login import *

#--------------------------------------------------------一些初始化的操作
#获取随机数的值
def get_myrandint():
    config_file=os.path.join(txt_dir,'randint_config.txt')
    if not os.path.exists(config_file):
        File().write_to_file(config_file,'w','1',next_line='N')
    myrandint=File().read_file_return_content(config_file)
    File().write_to_file(config_file,'w','%04d' % (int(myrandint)+1),next_line='N')
    return str(int(myrandint)+1)

# myrandint=get_myrandint()

#生成压缩包
def generate_zip_package(myrandint):
    package_file=os.path.join(testfile_dir,'package_%s.zip' % myrandint)
    File().move_file(os.path.join(testfile_dir,'package*.zip'),os.path.join(testfile_dir,'临时包'))
    os.chdir(txt_dir)
    Compress().zip(package_file,['randint_config.txt'])
    os.chdir(config_dir)

# generate_zip_package(myrandint)

#生成txt附件
def generate_txt_attachment(myrandint):
    txt_attach_file=os.path.join(testfile_dir,'attach_txt_%s.txt' % myrandint)
    File().move_file(os.path.join(testfile_dir,'attach_txt*.txt'),os.path.join(testfile_dir,'临时包'))
    File().write_to_file(txt_attach_file,'w','%s' % myrandint,next_line='N')

# generate_txt_attachment(myrandint)

#生成csv附件
def generate_csv_attachment(myrandint):
    csv_attach_file=os.path.join(testfile_dir,'attach_csv_%s.csv' % myrandint)
    File().move_file(os.path.join(testfile_dir,'attach_csv*.csv'),os.path.join(testfile_dir,'临时包'))
    File().write_to_file(csv_attach_file,'w','%s' % myrandint,next_line='N')

# generate_csv_attachment(myrandint)

#生成Word
def generate_word_attachment(myrandint):
    File().move_file(os.path.join(testfile_dir,'attach_word*.docx'),os.path.join(testfile_dir,'临时包'))
    doc=Document()
    doc.add_paragraph(myrandint)
    doc.save(os.path.join(testfile_dir,'attach_word_%s.docx' % myrandint))

# generate_word_attachment(myrandint)






if __name__ == "__main__":
    pass
