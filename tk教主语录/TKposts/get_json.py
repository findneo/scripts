from requests import * 
from time import *
import json
print asctime()
url="https://m.weibo.cn/api/container/getIndex?type=uid&value=1401527553&containerid=1076031401527553&page="
for i in range(1543,1,-1):
	u=url+str(i)
	f=open("result/%d.json"%i,'w+')
	f.write(get(u).content)
	f.close()
	sleep(2)
	if i%50==0:
		sleep(3)
print asctime()