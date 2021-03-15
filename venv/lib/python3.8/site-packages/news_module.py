def read_news(newlist):
#打印新闻列表
	for new_item in newlist:
		if isinstance(new_item, list):
			read_news(new_item)
		else:
			print(new_item)
