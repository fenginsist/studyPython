# import Exception
# except 在捕获错误异常的时候  只要根据具体的错误类型来捕获的
# 用一个块 可以捕获多个不同类型的异常
# Exception 可以捕获所有的异常  当对出现的问题或者错误不确定的情况下  可以使用Exception
# print(dir(Exception))


print('-----------------异常处理测试1: try-except方式')
# 将可能出错的代码放到try里面，except可以指定类型捕获异常。except里面的代码是捕获到异常时执行,将错误捕获，
# 这样程序就不会因为一段代码包异常而导致整个程序崩溃。
try:
    # print(b)        # 报错信息 ：name 'b' is not defined
    # li = [1, 2, 34] # 报错信息 ：list index out of range
    # print(li[10])
    a = 10 / 0  # division by zero
    pass
except NameError as msg:
    # 捕获到的错误 才会在这里执行
    print('NameError',msg)
    pass
except IndexError as msg:
    # 捕获到的错误 才会在这里执行
    print('IndexError',msg)
    pass
except ZeroDivisionError as msg:
    # 捕获到的错误 才会在这里执行
    print('ZeroDivisionError',msg)
    pass
except Exception as msg:  # 所有异常的基类
    # 在此尽量的去处理捕获到的错误
    print('Exception',msg)
    pass

print('初次接触异常处理')
print('HAHAHAHHAHA')

print('-----------------异常处理测试2:减少写try---except的麻烦')


def A(s):
    return 10 / int(s)
    pass


def B(s):
    return A(s) * 2


def main():
    # B(0)
    try:
        B('0')
        pass
    except Exception as msg:
        print(msg)
        pass
    pass


main()

# 不需要在每个可能出错的地方去捕获，只要在合适的层次去捕获错误就可以了 这样的话 就大大减少我们写try---except的麻烦

# 异常的抛出机制
# 如果在运行时发生异常  解释器会查找相应的异常捕获类型
# 如果在当前函数里面没有找到的话  它会将异常传递给上层的调用函数，看能否处理
# 如果在最外层 没有找到的话，解释器就会退出 程序down哦

print('-----------------异常处理测试3: try-except-else 方式')
# 没有捕获到异常时才执行else语句

try:
    print('我是没有错误产生的')
    a = 2/0
    pass
except SyntaxError as msg:
    print(msg)
except Exception as msg:
    print('error', msg)
else:
    print('当Try里面的代码 没有出现异常的情况下 我才会执行')
    pass

print('-----------------异常处理测试4: try-except-finally 方式')
# try-except-finally
try:
    int('34')
    open('aaaa.txt')
except Exception as msg:
    print(msg)
    pass
finally:
    print('不管有没有出错都执行的代码块')
    print('释放文件的资源、数据库连接是资源等等')
    pass
