#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time

remark = '''python操作excel用的xlrd和xlwt的用法'''

#引入相关包


#xlrd用法
import xlrd

#获取要操作的excel文档，formatting_info默认为False，设置为True，才可以读取合并单元格中的数据
xls = xlrd.open_workbook(r'D:\TDdownload\Document\Python\ExcelFile\test.xls',formatting_info=False)

#获取所有sheet名称，得到的是列表，例如：['Sheet1']
xls.sheet_names()

#获取特定sheet页，可用索引或者sheet名
sheet = xls.sheet_by_index(0)
sheet2 = xls.sheet_by_name('Sheet1')

#获取sheet页的名称、行数、列数
print(sheet.name,sheet.nrows,sheet.ncols)

#获取sheet页中整行或者整列的值，得到的是列表
rows = sheet.row_values(0)
cols = sheet.col_values(0)

#获取指定单元格的数据类型和内容，内容有时候需要用utf8编码（float，int等数据类型不需要）
#ctype值的含义 : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error， 6 blank（空白表格）
A1_tye = sheet.cell(0,0).ctype
A1_value = sheet.cell(0,0).value#.encode('utf8')#A1的值




#xlwt的用法
import xlwt

#创建要操作的excel文件对象
workbook = xlwt.Workbook(encoding='utf8')#这里W是大写

#创建要操作的sheet对象
worksheet = workbook.add_sheet('sheetname')

#设置字体和样式
font = xlwt.Font()#初始化创建字体
font.name = '宋体'#字体名
font.bold = False#是否加粗
font.underline = False#下户线
font.italic = False#斜体
style = xlwt.XFStyle()#初始化样式
style.font = font

#在某个位置写入内容，参数为：行，列，值
worksheet.write(0,0,'hello')#不带样式写入
worksheet.write(1,1,'hello',style)#带样式写入

#设置单元格宽度
worksheet.col(0).width = 3333#设置第一列的宽度

#输入一个日期到单元格
# 日期格式有:M/D/YY， D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss,
# M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
style.num_format_str = 'M/D/YY'
worksheet.write(2,2,time.localtime(),style)

#向单元格添加一个公式
#https://www.cnblogs.com/python-robot/p/9958352.html

#向单元格添加一个超链接:
worksheet.write(3, 3, xlwt.Formula('HYPERLINK("http://www.google.com";"Google")'))#后面的Google是展示名称

#合并列和行
# write_merge(x, x + m, y, w + n, string, style)
# x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示要写入的单元格内容，style表示单元格样式。其中，x，y，w，h，都是以0开始计算
worksheet.write_merge(4,4,4,5,'hello',style)#坐标分别为r1,r2,c1,c2，这里表示第四行，第四列和第五列合并

#设置单元格内容的对其方式
alignment = xlwt.Alignment() # Create Alignment
alignment.horz = xlwt.Alignment.HORZ_LEFT # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_BOTTOM # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style = xlwt.XFStyle()
style.alignment = alignment
worksheet.write(0, 0, 'Cell Contents', style)

#为单元格议添加边框（DASHED虚线，NO_LINE没有线，THIN实线）
# May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
# MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
borders = xlwt.Borders() # Create Borders
borders.left = xlwt.Borders.DASHED
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40
style = xlwt.XFStyle() # Create Style
style.borders = borders # Add Borders to Style
worksheet.write(6, 6, 'Cell Contents', style)

#为单元格设置背景色
# May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
pattern = xlwt.Pattern() # Create the Pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5
style = xlwt.XFStyle() # Create the Pattern
style.pattern = pattern # Add Pattern to Style
worksheet.write(7, 7, 'Cell Contents', style)

#保存
workbook.save(r'D:\TDdownload\Document\Python\ExcelFile\write.xls')






#xlutils的用法
import xlutils
from xlutils.copy import copy

#首先打开一个已经存在的文档
xlu = xlrd.open_workbook('filename.xls',formatting_info=True) #True代表保留原有格式，否则会转换成没有格式
new_xlu = copy(xlu)#复制一份xls对象，生成新的对象
#然后对new_xlu这个对象操作，最后保存
new_xlu.save('newname.xls')


print(xls.sheet_names())




if __name__=="__main__":
    pass