# 前言
每一个 study0X 分为若干个知识点

# 一、study01

# 二、study02

# 三、study03

# 四、study04

# 五、study05

# 六、study06

# 七、study07


# 八、常用命令

pip  list  查看安装的 包
pip show pygame(包名)  查看 包的路径


pip 安装的 包会在 python安装的路径下：D:\devApp\python\Lib\site-packages

查看包引用的位置  
import sys  
sys.path 此路径包含项目所有的包导入路径  
sys.path.append('\路径')  可以加入路径




# 九、总结使用的模块
```python
import random # 直接导入产生随机数的模块  
computer = random.randint(0, 2)

import time  # 引入第三方的时间模块
```

# 十一、数据类型可以使用的方法
len() 查看长度， 字符串、列表
index() 查找字符串的位置 ，字符串、列表
count(4) 统计元素出现的次数， 元组、列表
type() 查看数据的类型
字符串、列表、元组 都有下标

查一下。
range() 范围函数 ，生成一个范围的列表

不是很明白
hasattr()方法 ，在 study07 中的 单例模式中用到了，判断是否存在一个对象，


# 十一、常用魔术方法
1. 常用__init__(self) : 初始化 实例对象的 数据 。
2. 常用__new__(cls, *args, **kwargs) ： 创建对象 的方法，先执行这个，再执行 init 方法。
3. 常用__str__(self) ： 打印对象时 调用这个方法。
4. __class__(self: _T) -> Type[_T]: 获得已知对象的类 ( 对象.__class__)。
5. __del__(self)：对象在程序运行结束后进行对象销毁的时候调用这个方法，来释放资源。
6. 常用__call__(self)： 调用 实例对象() 方法 时 调用这个方法。

# 十二、常用魔术方法
1. _ _name_ _: 本类中  为 _ _main_ _ 字符串    

2. _ _all_ _: 在 类中 限制  from ... import 的导入 模块方法。

# 十三、常用注解

1. @classmethod  类方法注解
2. @staticmethod 静态方法注解
3. @property     getter方法
4. @方法名.setter setter 方法  











