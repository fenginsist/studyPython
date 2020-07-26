# 一、私有化属性
## 1. 引入私有化属性
问题：前面学习面向对象过程中，修改类属性都是直接通过类名修改的。如果有些重要属性不想让别人随便修改，或者防止意外修改，该怎么办？  
解决：为了更好的保存属性安全，即不能随意修改，将属性定义为 `私有属性`，添加一个可调用的方法去访问。

## 2. 语法（定义）
定义：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。 
```python
class Persion(object):
    __age = 18 # 定义一个私有化属性，属性名字前面加两个下划线
    pass
```
## 3. 私有属性的特性
特性1、私有化属性不能在类外面访问。
特性2、私有化属性可以在类里面访问，修改。
特性3、子类不能继承私有化属性。

## 4. 使用的场景
1.把特定的一个属性隐藏起来  不想让类的外部进行直接调用
2.我想保护这个属性 不想让属性的值随意的改变
3.保护这个属性   不想让派生类【子类】去继承

## 5. 最后小结
1.私有化的【实例】属性 不能再外部直接的访问  可以在类的内部随意的使用
2.子类不能继承父类的私有化属性【只能继承父类公共的属性和行为】
3.在属性名的前面直接加‘ __’  就可以变为私有化了

# 二、私有化方法
## 1. 概述
私有化方法跟私有化属性概念一样，有些重要的方法，不允许外部调用，防止子类意外重写，把普通的方法设置成私有化方法。

## 2. 语法
私有化方法，即在方法名前面加两个下划线。
示例
```python
class A(object):
    def __myname(self):
        pass
    pass
```

## 3. 特性
私有化方法一般是类内部调用，子类不能继承，外部不能调用。

## 4. 单下划线、双下划线、头双下划线、头尾双下划线说明
1. _xxx 前面加一个下划线，以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能使用from xxx import * 的方式导入。
2. __xxx__ 前后两个下滑线，魔法方法，一般是python自有，开发者不要创建这类型的方法。
3. __xxx 前面两个下划线，私有属性或者私有方法的定义。
4. xxx_ 后面单下滑线，避免属性名与python关键字冲突


# 三、property 属性
## 1. 引入 property 
通过前面的讲解，私有变量的访问，一般写两个方法一个访问，一个修改，由方法去控制访问。
例如:
```python
class P(object):
    def __init__(self):
        self.__age = 18 # 定义一个私有化属性，属性名字前加连个 __ 下滑线

    def get_age(self): # 访问私有类属性
        return self.__age

    def set_age(self,age): # 修改私有属性
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age
    pass
```
这样给调用者的感觉就是调用了一个方法，并不是访问属性。怎么做到让调用者直接以访问属性的方式，而且我们又能控制的方式提供给调用者？

## 2.  实现方式 1
'''
Python中有一个被称为属性函数(property)的小概念
示例：给age属性设置值时，会自动调用setage方法，获取age属性值时，会自动调用getage方法。
在上面的例如中最下面添加一句：age = property(get_age,set_age)
定义一个属性，当对这个age设置值时调用set_age,当获取值时调用get_age
注意：必须是以get,set开头的方法名，才能被调用
'''
xiaoming = P()
xiaoming.age = 15
print(xiaoming.age)

## 3. 实现方式 2
装饰器，即在方法上使用装饰器
案例：
```python
class P1(object):
    def __init__(self):
        self.__age = 18 # 定义一个私有化属性，属性名字前加连个 __ 下滑线

    @property  # 使用装饰器对age进行装饰，提供一个getter方法
    def age(self): # 访问私有类属性
        return self.__age

    @age.setter  # 使用装饰器进行装饰，提供一个setter方法
    def age(self,age): # 修改私有属性
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age
    pass
xiaoming = P1()
xiaoming.age = 15
print(xiaoming.age)
```

# 四、__new__(cls, *args, **kwargs) 方法
## 1. __new__方法的作用
创建并返回一个实例对象，如果__new__只调用了一次，就会得到一个对象。继承自object的新式类才有new这一魔法方法。

## 2. 注意事项：
1. __new__ 是在一个对象实例化的时候所调用的第一个方法  
2. __new__`至少必须要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供 ，其他的参数是用来直接传递给 __init__ 方法`
3. __new__ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，`如果 __new__ 没有返回实例对象，则 __init__ 不会被调用`
4. 在__new__ 方法中，不能调用自己的__new__ 方法，即：return cls.__new__ (cls)，否则会报错（RecursionError: maximum recursion depth exceeded：超过最大递归深度）

## 3. 使用方法
```python
class A(object):
    def __init__(self, a, b, c, k):
        print(a, b, c, k)
        print("__init__执行了")

    def __new__(cls, *args, **kwargs):
        print("__new__ 执行了")
        return object.__new__(cls) # 调用父类的new方法

a = A(1, 2365, 1122, k=3)
```
输出：
__new__ 执行了  
1 2365 1122 3  
__init__执行了  

## 4. 单例模式
1. 介绍：
单例模式是常用设计模式的一种，单例就比如我们打开电脑的回收站，在系统中只能打开一个回收站，也就 是说这个整个系统中只有一个实例，重复打开也是使用这个实例。  
简单的说就是不管创建多少次对象，类返回的对象都是最初创建的，不会再新建其他对象。

2. 实现步骤
利用类属性保存初次创建的实例对象，第二次实例化的时候判断类属性是否有保存实例对象，如果有就返回类属性保存的，如果没有就调用父类__new__方法创建新的实例对象。

代码实例 看 ch05_single单例模式.py

# 五、 错误与异常处理

## 1. 常用异常
异常	        导致的错误  
AssertionError	当assert语句失败时引发。  
AttributeError	当属性分配或引用失败时引发。  
EOFError	当input()函数达到文件结束条件时引发。  
FloatingPointError	当浮点运算失败时引发。  
GeneratorExit	调用生成器的close()方法时引发。  
ImportError	找不到导入的模块时引发。  
IndexError	当序列的索引超出范围时引发。  
KeyError	在字典中找不到键时引发。  
KeyboardInterrupt	当用户按下中断键(Ctrl+c或delete)时引发。  
MemoryError	当操作耗尽内存时引发。  
NameError	在局部或全局范围内找不到变量时引发。  
NotImplementedError	由抽象方法提出。  
OSError	当系统操作导致系统相关错误时引发。  
OverflowError	当算术运算的结果太大而无法表示时引发。  
ReferenceError	使用弱引用代理访问垃圾收集的引用时引发。  
RuntimeError	当错误不属于任何其他类别时引发。  
StopIteration	函数引发，以指示迭代器不再返回任何项。  
SyntaxError	遇到语法错误时由解析器引发。  
IndentationError	当缩进不正确时引发。  
TabError	当缩进由不一致的制表符和空格组成时引发。  
SystemError	当解释器检测到内部错误时引发。  
SystemExit	由sys.exit()函数引发。  
TypeError	将函数或操作应用于类型不正确的对象时引发。  
UnboundLocalError	当在函数或方法中引用局部变量，但没有将值绑定到该变量时引发。  
UnicodeError	当发生与unicode相关的编码或解码错误时引发。  
UnicodeEncodeError	当编码过程中发生与unicode相关的错误时引发。  
UnicodeDecodeError	当解码过程中出现与unicode相关的错误时引发。  
UnicodeTranslateError	翻译过程中发生与unicode相关的错误时引发。  
ValueError	当函数得到类型正确但值不正确的参数时引发。  
ZeroDivisionError	当除法或模运算的第二个操作数为零时引发。  

## 2. 引入异常
有时候代码写错了，执行程序的时候，执行到错误代码的时候，程序直接终止报错，
这是因为Python检测到一个错误时，解释器就无法继续执行了，出现了错误的提示，这就是"异常"。  
示例：变量b没有定义，直接打印变量b，会报异常。
## 3. 语法格式
try: 
    可能出现错误的代码块 
except: 
    出错之后执行的代码块 
else: 
    没有出错的代码块 
finally: 
    不管有没有出错都执行的代码块 

## 4. 异常类型
1. try ... except 语句  
将可能出错的代码放到try里面，except可以指定类型捕获异常。except里面的代码是捕获到异常时执行,将错误捕获，这样程序就不会因为一段代码包异常而导致整个程序崩溃。

2. try ... except ... else语句  
没有捕获到异常时才执行else语句
捕捉到异常时，else 语句不执行

3. try ... except ... finally语句
不管有没有步骤到异常 都会执行 finally语句

`代码实例 看  ch06_异常处理.py`

## 5. 自定义异常
1. 自定义异常，都要直接或间接继承Error或Exception类。
2. 由开发者主动抛出自定义异常，在python中使用raise关键字，

`代码实例 看  ch07_自定义异常.py`

# 六、动态添加属性和方法
## 1. 动态语言
动态语言：运行时可以改变其结构的语言，例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。  
如 `php,JavaScript,python都是动态语言，C，C#，java是静态语言。  `
所以`python可以在程序运行过程中添加属性和方法。  `

##2. 动态添加属性、方法
1. 动态添加实例属性  
实例对象.要添加的属性名=对应值。即可

1. 动态添加类属性  
类对象.要添加的属性名=对应值。即可

1. 动态添加实例方法 ： 添加方法需要 types 方法，先导入 import types  
实例对象.方法名 = types。MethodType（定义的方法名，实例对象） # 利用types方法绑定实例属性


1. 动态绑定类方法（@classmethod）和静态方法（@staticmethod）  ： 添加方法需要 types 方法，先导入 import types  
类对象.方法名 = 定义的方法名 （）

# 七、__slots__ 属性

## 1. 引入__slots__属性

python是动态语言，在运行的时候可以动态添加属性。

前面 一节说到 可以动态添加属性（实例属性、类属性）和方法（类方法、静态方法），如果要限制在运行的时候给类添加属性，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性。

只有在__slots__变量中的属性才能被添加，没有在__slots__变量中的属性会添加失败。可以防止其他人在调用类的时候胡乱添加属性或方法。__slots__属性子类不会继承，只有在当前类中有效。


## 2. __slots__ 的作用：
1. 限制要添加的实例属性
2. 节约内存空间