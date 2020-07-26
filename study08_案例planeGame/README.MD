# 一、需求描述
plane pro需求的描述：

存在四个对象：  
我方飞机、敌方飞机、我方子弹、敌方子弹  
功能:  

背景音乐的添加

我方飞机可以移动【根据按键来控制的】  
敌方飞机也可以移动【随机的自动移动】

双方飞机都可以发送子弹

步骤:
1. 创建一个窗口
2. 创建一个我方飞机 根据方向键左右的移动
3. 给我方飞机添加发射子弹的功能【按下空格键去发送】
4. 创建一个敌人飞机
5. 敌人飞机可以自由的移动
6. 敌人飞机可以自动的发射子弹


# 二、安装pygame时注意的问题
在安装pygame模块的时候尤其要注意一下：

如果在pychram中安装不成功  如下错误：  
EOFError: EOF when reading a line

----------------------------------------  
Command "python setup.py egg_info" failed with error code 1 in C:\Users\Administrator\AppData\Local\Temp\pip-install-392v1at0\pygame\

此时我们就可以换种思路：

1. 确保在系统层面的python环境里面 已经安装了pygame[pip install pygame] 一般都可以安装成功
2. 我们就可以把 已经安装好的 pygame 模块的 文件夹拷贝到 pycharm 所创建项目中的venv虚拟环境里面【E:\PythonPro\PlaneDemo\venv\Lib\site-packages】

soure path：D:\devApp\python\Lib\site-packages  
dst path: 你的项目路径/venv\Lib\site-packages

# 三、


 
  

