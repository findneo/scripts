# -*- coding:utf-8 -*-
from os import system
import time


def banner():
    print '''
             ___
            / __)
 ____   ___| |__ ___   ____ _   _  ___
|  _ \ /___)  __) _ \ / ___) | | |/___)
| | | |___ | | | |_| ( (___| |_| |___ |
|_| |_(___/|_|  \___/ \____)\____(___/  
***********************************************************
        欢迎使用网站监测助手
功能：
    每隔十分钟用ie浏览器按照网站列表依次打开各网站

用法：
    1、把网站列表放在本程序同目录下的sites.txt文件里
    2、每行一个网站，建议带上协议[http://或https://]
    3、运行本程序

环境：
    Windows

建议：
    1、浏览IE时可空格键翻页
    2、alt+space+c可快速关闭当前浏览器页面
    3、ctrl+c退出程序

                                    made by findneo
                                    2017/8/17 12:56
***********************************************************
    '''


def mon():
    sites = []
    with open('sites.txt', 'r') as f:
        for i in f.readlines():
            sites.append(i.strip('\n\t '))
    banner()

    while 1:
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in sites:
            system('"C:\Program Files\Internet Explorer\IEXPLORE.EXE" ' + i)
        print "过会儿再来检查吧..."
        time.sleep(600)


if __name__ == '__main__':
    try:
        mon()
    except Exception as e:
        banner()
        system("pause")
