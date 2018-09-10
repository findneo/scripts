#coding:utf8
import json
import re

def parse_cards_to_html(data_cards):
	"""
	微博API
	(https://m.weibo.cn/api/container/getIndex?type=uid&value=1401527553&containerid=1076031401527553&page=1)
	返回的一个字典，形如
	{	ok: 1,
	data: 
	{	cardlistInfo: {...},
		cards: 
		[	{	card_type: 9,	
				itemid: foo,	
				scheme: post链接,
				mblog: {created_at: post发表时间,	...,
						text: post内容,		...,
						retweeted_status: {created_at: repost发表时间,...,text: repost内容,...,}
						},
				show_type: 0
			},
			{...},...
		],
		showAppTips: 0,
		scheme: foo
	}
}
	本函数的功能是将cards中每一个表示post的card里的时间和内容，以及repost的时间和内容(如果有的话)，提取出来，
	构造成HTML语句。
	"""
	ret=""
	for card in data_cards:
		if card["card_type"]==9: 
			# card_type==9 说明当前card是一个post
			is_repost=0
			post=card["mblog"] 
			post_time=post["created_at"]
			post_text=post["text"]
			ret0="<p><code><br />%s</code><br />%s</p>"%(post_time,post_text)
			if "retweeted_status" in post.keys():
				# 当前card中有retweeted_status键说明这是一个repost
				is_repost=1
				repost=post["retweeted_status"]
				repost_time=repost["created_at"]
				repost_text=repost["text"]
				ret1="\n\t<blockquote><p><code>%s</code><br />%s</p></blockquote>"%(repost_time,repost_text)
			ret=ret+ret0+ret1 if is_repost else ret+ret0
			ret=ret+"<hr />\n"
	return ret


def comment_img_in_html(file_name):
	"""
	因为教主post中时有图片，15000+条post里的图片数量相当可观（而且很多加载不出来），
	为了提高加载速度，这个函数将成品中的img标签全部注释掉。
	"""
	with open(file_name) as old_f,open("noimg_%s"%file_name,"w+") as new_f:
		for line in old_f.readlines():
			res=re.sub('(<img.*?>)',r"<!--\1-->",line)
			new_f.write(res)

def main():
	with open("tkposts.html","w+") as f:
		head='<html><head><style type="text/css">html{background:#f2f2f2;font-size:16px;font-family:Monaco}</style><title>TK POSTS</title></head><body>\n'
		f.write(head.encode('utf8'))
		for i in xrange(1,1543):
			data = json.load(open("%d.json"%i))
			if data["ok"]!=1:
				print "%d.json no data"%i
				continue
			msg_list=data["data"]["cards"]
			msg_html=parse_cards_to_html(msg_list)
			f.write(msg_html.encode('utf8'))
		tail="</body></html>"
		f.write(tail.encode('utf8'))
	comment_img_in_html("tkposts.html")

if __name__ == '__main__':
	"""
	截至 2018/3/8 下午一时许，教主在新浪微博上共发表约13831条状态，
	其中约6157条是转发自己或其他人的状态并评论。
	第一条发布在2010-05-21，内容是
	“刚看到的：2007年德国《自然科学》杂志的一篇文章指出，
	最近感染过弓形虫的女性怀孕生男孩的概率为60.8%。也就是说，
	感染弓形虫有助于生儿子——不过，不知道是需要在感染状态才行，还是治好了也行。 ​​​”，
	可以看到风格很早就形成了，幽默感，批判性，科学性具存，这就是让人乐于追随学习的地方。
	"""
	main()
