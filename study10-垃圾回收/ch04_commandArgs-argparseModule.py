import argparse

# 创建一个解析器对象
parse = argparse.ArgumentParser(prog='my - 我自己的程序', usage='%(prog)s [options] usage',
                                description='my-编写自定义命令行的文件', epilog='my - epilog')

# print(parse.print_help()) # 会打印 很多，帮助的用法

# 添加位置参数【必选参数】
parse.add_argument(dest='name', type=str, help='你自己的名字')
parse.add_argument(dest='age', type=str, help='你的年龄')

# 添加可选参数  默认会用’-‘来认证可选参数，剩下的即为位置参数， 位置参数必须传。
# -s: 可选
# action='append'： 表示 限定输入的值,  存为列表，可以有多个参数
# parse.add_argument('-s', '--sex', action='append', type=str, help='你的性别')
# 限定一个范围
parse.add_argument('-s', dest='--sex', default='男', choices=['男', 'femal', '女', 'male'], type=str, help='你的性别')
# # print(parse.print_help())

# 开始解析参数
result = parse.parse_args()
print(result)
print(result.name,result.age,result.sex)
