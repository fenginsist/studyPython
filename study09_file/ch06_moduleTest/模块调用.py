import moduleTest  # 导入模块  第一种导入方式
from moduleTest import add  # 第二种导入方式
from moduleTest import *  # 第三种导入方式

# 以上三种相对路径导入方式 视频里正常 ，我这里爆红，但是可以使用
# 这里我使用下面的 三种绝对路径的导入方式

import study09_file.ch06_moduleTest.moduleTest
from study09_file.ch06_moduleTest.moduleTest import add
from study09_file.ch06_moduleTest.moduleTest import *

print(moduleTest.add(1, 3))
print(moduleTest.diff(5, 1))
print(moduleTest.printInfo())  # 尽管不在 __all__ 中 也可以调用, 是因为导入的方式  impot XXX

print(add(1, 3))
print(diff(5, 1))
print(printInfo())  # #对于这种情况 就不能使用了 因为没有在__all__中, 是因为导入的方式 from XXX impot
