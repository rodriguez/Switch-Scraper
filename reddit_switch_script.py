import praw
from twilio.rest import Client
import json 
from json_handler import post_dic
from creds import *

client = Client(account_sid, auth_token)

reddit = praw.Reddit(client_id=cid,
                     client_secret=secret,
                     password=password,
                     user_agent='testscript by /u/Arod16',
                     username=username)

def dic_deal(title):
	global post_dic
	if title not in post_dic:
		post_dic[title] = False
		print("New Post to Dic: ", title)
		print(post_dic[title])

def clean(title):
	string = ""
	lower_range = range(97, 123)
	upper_range = range(65, 91)
	numbers = range(48, 58)
	special = ["$", ".", " "]
	for char in title.lower():
		if ord(char) in lower_range or ord(char) in upper_range or ord(char) in numbers or char in special:
			string += char
	return string

def twilioApi(title, link, number):
	global client
	message = client.messages.create(
    to="+1" + number, 
    from_="+16232445451",
    body=title + " --> " + link)
	print(message.sid)

def parser(title):
	if post_dic[title] == True:
		return True
	if "switch" in title:
		money_index = title.find("$")
		if money_index != -1:
			money_string = ""
			money_index += 1
			eof = [".", " ", ""]
			while money_index < len(title) and title[money_index] not in eof:
				money_string += title[money_index]
				money_index += 1
			price = int(money_string)
			if price > 200:
				return False
	return True

i = 0
number = input("What is your number?: ")

while True:
	i += 1
	for post in reddit.subreddit('NintendoSwitchDeals').new():
		title = post.title
		link = post.shortlink
		clean_title = clean(title)
		dic_deal(clean_title)
		flag = parser(clean_title)
		if flag == False:
			post_dic[clean_title] = True
			twilioApi(title, link, number)
	print("Running: ", i, "time(s)")
	with open("nsd_posts.json", "w") as f:
		f.write(json.dumps(post_dic))


