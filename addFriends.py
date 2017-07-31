#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import _sqlite3
from wxpy import *
import logging

#init
bot = Bot(cache_path=True)
# console_qr=True

cx = _sqlite3.connect("tickets.db")
sql = "select wechatID from TB_TICKETINFO where wechatID != ''"
cursor = cx.execute(sql)

for row in cursor:
	try:
		print("adding row[0]: ",row[0])
		print(type(row[0]))
		log=bot.add_friend(str(row[0]),verify_content='Adding friends')
		print("after adding one",log)
	except:
		print("Already adding this id or this ID not exists")

embed()

# bot.add_friend("jason-yang911",verify_content='Adding friends')

