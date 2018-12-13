import praw
from twilio.rest import Client
import json 
from json_handler import post_dic
from creds import *
import time

import pymongo
from pymongo import MongoClient


twi_client = Client(account_sid, auth_token)

reddit = praw.Reddit(client_id=cid,
                     client_secret=secret,
                     password=password,
                     user_agent='testscript by /u/Arod16',
                     username=username)

# db_client = MongoClient()
def dic_deal(title):
	global post_dic
	if title not in post_dic:
		post_dic[title] = False
		print("New Post to Dic: ", title)

def clean(title):
	string = ""
	lower_range = range(97, 123)
	upper_range = range(65, 91)
	numbers = range(48, 58)
	for char in title.lower():
		if ord(char) in lower_range or ord(char) in upper_range or ord(char) in numbers or char == "$":
			string += char
		else:
			string += " "
	return string

def twilioMessage(title, link, number):
	global twi_client
	message = twi_client.messages.create(
    to="+1" + number, 
    from_="+16232445451",
    body=title + " --> " + link)
	print(message.sid)

def parser(title):
	if post_dic[title] == True:
		return True
	if "switch" in title:
		money_indices = []
		iter_title = title
		money_index = iter_title.find("$")
		while money_index != -1:
			ints = money_index+1
			string = ""
			while ints < len(iter_title) and iter_title[ints].isdigit() == True:
				string += iter_title[ints]
				ints += 1
			money_indices.append(int(string))
			money_index = iter_title.find("$", ints)
		if len(money_indices) != 0:
			price = max(money_indices)
			if price > 200:
				return False
	return True

# def updateDB(clean, old, link):
# 	global db_client
# 	db = db_client.pymongo_db
# 	col = db.pymongo_col
	

i = 0
number = input("What is your number? ")

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
			twilioMessage(title, link, number)
		# updateDB(clean_title, title, link)
	print("Running: ", i, "time(s)")
	with open("nsd_posts.json", "w") as f:
		f.write(json.dumps(post_dic))
	time.sleep(30)


