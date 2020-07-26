# 文件备份

def copyFile():
    old_file = input('请输入要备份的文件名：')
    file_list = old_file.split('.')
    new_file = file_list[0] + '_备份.' + file_list[1]

    olf_f = open(old_file, 'r')
    new_f = open(new_file, 'w')
    data = olf_f.read()
    new_f.write(data)

    olf_f.close()
    new_f.close()
    pass


copyFile()


def copyBigFile():
    # 接收用户输入的文件名
    old_file = input('请输入要备份的文件名:')
    file_list = old_file.split('.')
    # 构造新的文件名.加上备份的后缀
    new_file = file_list[0] + '_备份.' + file_list[1]
    try:
        # 监视啊哟处理的逻辑
        with open(old_file, 'r') as old_f, open(new_file, 'w')as new_f:
            while True:
                content = old_f.read(1024)  # 一次读取1024字符
                new_f.write(content)
                if len(content) < 1024:
                    break
    except  Exception as msg:
        print(msg)
    pass
