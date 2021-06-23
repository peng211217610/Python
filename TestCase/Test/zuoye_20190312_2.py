#被引入的包不在本Python文件同目录下,先将包路径添加到Pythonpath里
import sys
sys.path.append(r'D:\TDdownload\Document\Python\test')

import phone.apple.iphone6 as ip6Price
import phone.apple.iphone7 as ip7Price
import phone.samsung.note.galaxy_note8 as no8Price
import phone.samsung.s.galaxy_s7 as s7Price

#iphone6价格
ip6Price.askPrice()
#iPhone7价格
ip7Price.askPrice()
#note8价格
no8Price.askPrice()
#s7价格
s7Price.askPrice()