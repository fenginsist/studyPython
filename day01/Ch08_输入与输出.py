# 输出 % 占位符  \n换行效果

print('--------------输出方式一：%占位符---------------')
me = '我的'
classPro = '清华附中一年级3班'
age = 7
print('%s名字是小明：来自【%s】, 今年%d 岁了' % (me, classPro, age))
print('%s名字是胖虎：来自【%s】, 今年%d 岁了' % (me, classPro, age))
print('%s名字是小叮当：来自【%s】, 今年%d 岁了' % (me, classPro, age))
print('我可以\n换行吗')  # \n换行效果

print()
print('练习输出')
'''
练习输出
姓名：老夫子
QQ：666666
手机号： 17862970812
公司地址： 山东省济宁市
'''
name = '老夫子'
QQ = '666666'
phone = '17862970812'
addr = '山东省济宁市'
print('姓名：%s \nQQ:%s \n手机号：%s \n公司地址：%s'%(name, QQ, phone, addr))

print('--------------输出方式二：.format()---------------')
print('姓名：{} \nQQ:{} \n手机号：{} \n公司地址：{}'.format(name, QQ, phone, addr))


print('--------------输入方式---------------')
# input的练习  获取键盘输入的内容
nameInput=input("请输入您的姓名:")
ageInput=int(input("请输入您的年龄:"))
print(type(nameInput))
QQInput=input('请输入您的qq')
phoneInput=input("请输入您的电话:")
addrInput=input("请输入您的地址:")

print('姓名:%s 年龄是:%d 岁'%(nameInput,ageInput))
# print('姓名:{} 年龄是:{} 岁'.format(name,age))
print('QQ:{}'.format(QQInput))
print('手机号:{}'.format(phoneInput))
print('地址:{}'.format(addrInput))