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
        ��ӭʹ����վ�������
���ܣ�
    ÿ��ʮ������ie�����������վ�б����δ򿪸���վ

�÷���
    1������վ�б���ڱ�����ͬĿ¼�µ�sites.txt�ļ���
    2��ÿ��һ����վ���������Э��[http://��https://]
    3�����б�����

������
    Windows

���飺
    1�����IEʱ�ɿո����ҳ
    2��alt+space+c�ɿ��ٹرյ�ǰ�����ҳ��
    3��ctrl+c�˳�����

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
        print "�������������..."
        time.sleep(600)


if __name__ == '__main__':
    try:
        mon()
    except Exception as e:
        banner()
        system("pause")
