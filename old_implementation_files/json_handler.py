import json

post_dic = {}

with open("nsd_posts.json", "r") as f:
	post_dic = json.load(f)
