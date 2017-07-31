Implemented:
loading username from excel to database
automatic reply to the user, if hit keyword, invite user to group chatting


Usage:
python3 robotclient.py
	auto accept friends and invite them to group chatting if they know the key word
python3 dboperate.py
	load data from excel to database
sqlite3 tickets.db
	select * from TB_TICKETINFO;
	.schema TB_TICKETINFO
	DROP TABLE TB_TICKETINFO;

Requirements:
install xlrd
	pip install xlrd

Reference:
	https://github.com/youfou/wxpy
