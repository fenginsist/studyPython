import sys

print('参数个数为:', len(sys.argv), '个参数.')
print('参数列表类型:', type(sys.argv))
print('参数列表:', str(sys.argv))
print('参数列表:', str(sys.argv[1:]))  # 对参数 进行切片

# 在命令行 模式下输入以下命令 测试：
# python ch03_commandArgs-sysModule.py 1 2 3

# 输出：
'''
参数个数为: 4 个参数.
参数列表类型: <class 'list'>
参数列表: ['ch03_commandArgs-sysModule.py', '1', '2', '3']
参数列表: ['1', '2', '3']
'''
