# -*- coding=utf-8 -*-
import win32api
import win32con
import time
import sys


def sshot():  # 通过模拟发送win+print击键来截图
    win32api.keybd_event(0x5B, 0, 0, 0)  # 0x5B is keyCode for left win
    win32api.keybd_event(0x2C, 0, 0, 0)  # 0x2C is keyCode for print Screen
    win32api.keybd_event(0x5B, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x2C, 0, win32con.KEYEVENTF_KEYUP, 0)
    # 依次按下左win,按下print,松开左win,松开print


def main():
    print """
    ************************************************************
    在你欣赏电影时我会自动帮你截屏，你可以在图片目录中找到图片。
    两分钟后开始截屏，每十分钟截一张，四个小时后自动停止 :)
                                        made by findneo 
                                        2017/8/17 13:13
    ************************************************************
    """
    initInterval = 2 * 60
    interval = 10 * 60
    uplimitt = 4 * 60 * 60
    sys.stdout.write('##')
    time.sleep(initInterval)  # 电影开始后initInterval秒后截下第一张图
    sshot()
    i = 0
    while 1:
        sys.stdout.write('##')
        time.sleep(interval)
        # 每隔interval秒截一张图
        sshot()
        i += 1
        if i * interval > uplimitt:  # 如果你忘了退出程序，那么4个小时候它会自己退出
            return 0


if __name__ == '__main__':
    main()
