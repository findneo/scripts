# 为乌云知识库生成目录
import os
f0 = open('index.html', 'w')
cnt = 1
list = os.listdir('drops')
for i in range(0, len(list)):
    path = os.path.join('drops', list[i])
    if os.path.isfile(path):
        f = open(path, 'r')
        t = 0
        for li in f.readlines():
            t = t + 1
            if t == 5:
                f0.write('<li><a href="' + path + '">' +
                         '\t' + li[9:-27] + '</a></li>' + '\n')
                break
        cnt = cnt + 1
        f.close()

f0.close()
print cnt
