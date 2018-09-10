#coding:utf8
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
from bs4 import BeautifulSoup
import requests
import base64
# 配置用户ID，可登陆后查看地址栏获取
username="findneo"
# 配置cookies，有些记录可能设置为仅自己可见，那么就需要登陆来获取完整记录
# cookie中只要有dbc12就可以表明身份
cookies=dict()
# cookies=dict(dbcl2="xxxxxxxxxxxxxxxxxxx")

def parse(url):
	r=requests.get(url,cookies=cookies)
	s=BeautifulSoup(r.content,'lxml')
	one_page=s.find_all(name='a',attrs={'class':'nbg'})
	return one_page

def main():
	url="https://movie.douban.com/people/%s/collect"%username
	page_url="https://movie.douban.com/people/findneo/collect?start=%d"
	r=requests.get(url,cookies=cookies)
	movie_num=int(BeautifulSoup(r.content,'lxml').title.string[12:-2])
	each_page=15
	page_num=movie_num/each_page+(movie_num%each_page!=0)
	# page_num=1
	f=open('res.html','w+')
	content=[]
	for i in xrange(page_num):
		purl=page_url%(each_page*i)
		content+=parse(purl)
	html="""
		<html>
			<head>
				<style type="text/css">img{ width: 10%%; height: 33.3%%; display: block; float: left;}</style>
			</head>
			<body>
			<title> %s's movie(%d)</title>\n%s
			</body>
		</html>
	"""%(username,movie_num,'\n'.join(map(str,content)))
	"<html><body><title>douban</title>%s"
	f.write(html)

def img2base64(infile,outfile):
	inf=open(infile)
	s=BeautifulSoup(inf,'lxml')
	for i in s.find_all('img'):
		i['src']="data:image/jpeg;base64,%s"%base64.b64encode(requests.get(i['src']).content)
	open(outfile,'w+').write(str(s))

if __name__ == '__main__':
	# 在当前目录下生成res.html
	main()
	# 将所有图片下载并用base64编码存储，加载时就无需从豆瓣再获取图片。
	# img2base64('res.html','out.html')