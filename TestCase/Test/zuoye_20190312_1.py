'''
附件里压缩 了一个目录（见附件phone.zip），解压后结构如下。

phone
  ├─apple
  └─samsung
      ├─note
      └─s
这个目录里面对应了苹果、三星手机 的价格。
在相应目录里面，包含对应手机价格的python文件。
请同学们在维持目录结构不变的前提下，把这个目录结构做成名为python包。

然后，自己写一个Python程序调用 那个python包里面的每个
模块文件（共四个）里面的askPrice 函数，显示每种手机的价格

同学们先将那个phone包，和自己写的调用程序文件放在同一个目录下，
运行调用程序，显示各种手机价格

同学们再将那个phone包，和自己写的调用程序文件放在不同的目录下，
通过设置 sys.path 或者 环境变量PYTHONPATH，
来保证可以找到phone包，并成功调用。

'''
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









