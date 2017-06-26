#-*- coding=utf-8 -*-
import win32gui,win32api,win32con  
import time
import sys
 
def sshot():#通过模拟发送win+print击键来截图
	win32api.keybd_event(0x5B,0,0,0) #0x5B is keyCode for left win
	win32api.keybd_event(0x2C,0,0,0) #0x2C is keyCode for print Screen
	win32api.keybd_event(0x5B,0,win32con.KEYEVENTF_KEYUP,0)  
	win32api.keybd_event(0x2C,0,win32con.KEYEVENTF_KEYUP,0)
	#依次按下左win,按下print,松开左win,松开print
def main():
	print r"just go or movie,I will shot screen automatically for u!"
	initInterval= 2*60
	interval = 10*60
	uplimitt= 4*60*60
	sys.stdout.write('##')
	time.sleep(initInterval)#电影开始后initInterval秒后截下第一张图
	sshot()
	i=0
	while 1:  
		sys.stdout.write('##')
		time.sleep(interval) 
		#每隔interval秒截一张图
		sshot()
		i+=1
		if i*interval>uplimitt:#如果你忘了退出程序，那么4个小时候它会自己退出
			return 0
if __name__ == '__main__':
    main()
