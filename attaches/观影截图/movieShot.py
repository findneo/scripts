# -*- coding=utf-8 -*-
import win32api
import win32con
import time
import sys


def sshot():  # ͨ��ģ�ⷢ��win+print��������ͼ
    win32api.keybd_event(0x5B, 0, 0, 0)  # 0x5B is keyCode for left win
    win32api.keybd_event(0x2C, 0, 0, 0)  # 0x2C is keyCode for print Screen
    win32api.keybd_event(0x5B, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x2C, 0, win32con.KEYEVENTF_KEYUP, 0)
    # ���ΰ�����win,����print,�ɿ���win,�ɿ�print


def main():
    print """
    ************************************************************
    �������͵�Ӱʱ�һ��Զ�����������������ͼƬĿ¼���ҵ�ͼƬ��
    �����Ӻ�ʼ������ÿʮ���ӽ�һ�ţ��ĸ�Сʱ���Զ�ֹͣ :)
                                        made by findneo 
                                        2017/8/17 13:13
    ************************************************************
    """
    initInterval = 2 * 60
    interval = 10 * 60
    uplimitt = 4 * 60 * 60
    sys.stdout.write('##')
    time.sleep(initInterval)  # ��Ӱ��ʼ��initInterval�����µ�һ��ͼ
    sshot()
    i = 0
    while 1:
        sys.stdout.write('##')
        time.sleep(interval)
        # ÿ��interval���һ��ͼ
        sshot()
        i += 1
        if i * interval > uplimitt:  # ����������˳�������ô4��Сʱ�������Լ��˳�
            return 0


if __name__ == '__main__':
    main()
