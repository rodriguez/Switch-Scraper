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

db_client = MongoClient()
db = db_client.switch_db
deals = db.deals

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

def parser_for_valid_deal(title, in_db):
	if in_db == True:
		return False # we already saw this; if we didn't act on it before, we're not going to now
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
				return True # new deal with target price (probably a Switch deal)
	return False # new deal but probably not a Switch deal (price not high enough)

def updateDB(clean, old, link):
	global db_client, db, deals
	pair = {"title": clean}
	lookup = db.deals.find_one(pair)
	if lookup == None:
		doc = {"title": clean, "old_title": old, "link": link}
		db.deals.insert_one(doc)
		return False
	return True	

i = 0
number = input("What is your number? ")

while True:
	i += 1
	for post in reddit.subreddit('NintendoSwitchDeals').new():
		title = post.title
		link = post.shortlink
		clean_title = clean(title)
		in_db = updateDB(clean_title, title, link)
		is_valid_deal = parser_for_valid_deal(clean_title, in_db)
		if is_valid_deal == True:
			print("found a valid deal", title)
			# twilioMessage(title, link, number)
	print("Running: ", i, "time(s)")
	# time.sleep(30)

