#-*- coding:utf-8 -*-
import os
os.system("ipconfig")
oneip = raw_input("\n\nÇëÊäÈëÄãµÄip:")
prefix = oneip[:-len(oneip.split('.')[-1])]
print prefix
for i in range(1,256):
    os.system("echo " + prefix + str(i) + "&ping -n 1 -w 1 " +
              prefix + str(i) + "|findstr 100%")
    if i%15==0:
        os.system("pause")
