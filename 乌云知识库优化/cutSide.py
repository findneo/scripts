# 不知为何，知识库页面边上有黑边，影响比较大
# 因此想把他们去掉
import os
cnt = 1
list = os.listdir('drops')
for i in range(0, len(list)):
    path = os.path.join('drops', list[i])
    if os.path.isfile(path):
        with open(path, 'r') as f:
            with open(os.path.join('newdrops', list[i]), 'w+') as f0:
                t = 0
                for li in f.readlines():
                    t = t + 1
                    if t == 149:
                        f0.write("  width: 0px;\n")
                    elif t == 268:
                        f0.write("  height: 0px;\n")
                    elif t == 280:
                        f0.write("  width: 0px;\n")
                    elif t == 291:
                        f0.write("  line-height: 0px;\n")
                    else:
                        f0.write(li)
        cnt = cnt + 1
        if cnt % 5000 == 0:
            print cnt
print cnt
