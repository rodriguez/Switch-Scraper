import praw
from twilio.rest import Client
import json 
from json_handler import post_dic

account_sid = "AC68ecdb4047ae378eececca3f44006f66"
auth_token = "da1b49fcccca917c0ed00379c7e16447"
client = Client(account_sid, auth_token)

cid = 'FlluXmW8byy8YQ'
secret = 'NL3t0HaJuf0vKNLbE93CZ6bxPK0'

reddit = praw.Reddit(client_id=cid,
                     client_secret=secret,
                     password='paugasol16',
                     user_agent='testscript by /u/Arod16',
                     username='Arod16')

def dic_deal(title):
	global post_dic
	if title not in post_dic:
		post_dic[title.lower()] = False

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

def twilioApi(title, link):
	global client
	message = client.messages.create(
    to="+12033088233", 
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
			twilioApi(title, link)
	print("Running: ", i, "time(s)")

with open("nsd_posts.json", "w") as f:
	f.write(json.dumps(post_dic))


