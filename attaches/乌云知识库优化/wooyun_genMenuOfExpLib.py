# 为乌云漏洞库生成目录
import os
f0 = open('index.html', 'w')
# f.write('Hello, world!')
cnt = 1
list = os.listdir('bugs')
for i in range(0, len(list)):
    path = os.path.join('bugs', list[i])
    if os.path.isfile(path):
        f = open(path, 'r')
        t = 0
        for li in f.readlines():
            t = t + 1
            if t == 6:
                f0.write('<li><a href="' + path + '">' +
                         '\t' + li[7:-22] + '</a></li>' + '\n')
                break
        cnt = cnt + 1
        f.close()
f0.close()
print cnt
# 40294 means success
# this script cost about 1min or so
