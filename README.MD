# 前言
每一个 study0X 分为若干个知识点

# 一、study01
1. helloword
2. 数据类型
3. 变量
4. 算数运算符
5. 比较运算符
6. 逻辑运算符
7. 赋值运算符
8. 输入与输出

# 二、study02 逻辑循环
1. 单分支
2. 双分支
3. 多分支
4. 多分支多条件
5. if-else嵌套
6. WhileLoop循环
7. forLoop循环
8. 案例

# 三、study03 数据类型详解
1. 字符串str
2. 集合list
3. 元组 tuple
4. 字典 dict
5. 公用方法

# 四、study04 方法、参数
1. 方法定义
2. 方法参数：必选参数、可选参数、可变参数
3. 方法返回值
4. 函数嵌套
5. 案例
6. 全局与局部变量
7. 引用
8. 匿名函数-lambda表达式
9. 内置函数

# 五、study05 面向对象上
1. 创建类
2. 魔术方法 __init_ _
3. self 关键字
4. 其他常用魔术方法
5. 案例
6. 作业

# 六、study06面向对象中
1. 析构函数
2. 继承
3. 多继承
4. 间接继承
5. 重写和调用父类方法
6. 多态
7. 类属性和实例属性
8. 类方法和静态方法

# 七、study07 面向对象下 异常、私有
1. 属性私有化
2. 方法私有化
3. 属性函数 property
4. new 实例化
5. single 单例模式
6. 异常处理
7. 自定义处理
8. 动态添加属性
9. slots属性限制
课后作业

# 八、study08 飞机游戏案例

# 九、study09 文件操作
1. 读写模式
2. 案例：copyFile
3. 文件定位
4. 文件导入
5. os 模块
6. module
7. 创建模块

# 十、study10 垃圾回收
直接看代码吧

# 十一、study11 正则表达式
1. regix_study
2. ch03_常用匹配规则-匹配字符.py
3. ch04_常用匹配规则-匹配字符数量.py
4. ch05_常用匹配规则-原生字符串.py
5. ch06_常用匹配规则-匹配开头和结尾.py
6. ch07_常用匹配规则-分组匹配.py
7. ch08_reModuleOtherMethod.py
8. ch09_贪婪模式和非贪婪模式.py
9. ch10_homework1.py
10. ch11_homework2.py


# 八、常用命令

1. pip  list  查看安装的 包
2. pip show pygame(包名)  查看 包的路径

3. pip 安装的 包会在 python安装的路径下：D:\devApp\python\Lib\site-packages

4. 查看包引用的位置  
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
1. len() 查看长度， 字符串、列表
2. index() 查找字符串的位置 ，字符串、列表
3. count(4) 统计元素出现的次数， 元组、列表
4. type() 查看数据的类型
5. 字符串、列表、元组 都有下标

6. range() 范围函数 ，生成一个范围的列表

不是很明白
7. hasattr()方法 ，在 study07 中的 单例模式中用到了，判断是否存在一个对象，


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











