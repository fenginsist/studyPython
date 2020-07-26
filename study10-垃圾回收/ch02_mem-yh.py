print('----------------小整数对象的删除测试')
a=140
b=140
print(id(a))
print(id(a))

del a  # 删除 对象
del b
c=140
print(id(c))

print('----------------大整数对象的删除测试：与小整数测试一样')

biga=100000
bigb=100000
print(id(biga))
print(id(bigb))
del biga
del bigb
bigc=100000
print(id(bigc))

# 大整数池和小整数池的区别是：
# 1 从结果来看是一样的
# 2 大整数池是没有提前的创建好对象，是个空池子，需要我们自己去创建
# 创建好之后，会把整数对象保存到池子里面，后面都不需要再创建了 直接拿来使用
# 小整数池是提前将【-5,256】的数据都提前创建好
# 字符串的驻留共享机制intern机制

print('---------------- ')
sa='ab_c'
sb='ab_c'
sc='ab_c'
sd='ab_c'

sa="a!b"
sb="a!b"
sc="a!b"
sd="a!b"
print(sa is sb)
print(id(sa))
print(id(sb))
print(id(sc))
print(id(sd))
