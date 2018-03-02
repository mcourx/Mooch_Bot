import time, praw, re, pdb, os, praw, datetime
from datetime import date

r = praw.Reddit('bot1', user_agent="Steph 0.1")

def calculate(inp):
	unit = ""
	r = re.compile("\d+")
	initial_value = float("".join(r.findall(inp)))

	if "days" in inp:
		n = initial_value /6
		unit = "days"
	elif "months" in inp:
		n = initial_value /6*30
		unit = "months"
	elif "years" in inp:
		n = initial_value /6*365
		unit = "years"
	else:
		run_bot()

	final = round(n, 2)

	return final, initial_value, unit

def diff(comment):
	r2 = re.compile("\d\d\/\d\d\/\d\d\d\d/*")
	t2 = r2.findall(comment)
	print(t2)
	before = list(t2[0])
	after = list(t2[1])
	b_year = int("".join(before[6:10]))
	a_year = int("".join(after[6:10]))
	b_month = int("".join(before[0:2]))
	a_month = int("".join(after[0:2]))
	a_day = int("".join(after[3:5]))
	b_day = int("".join(before[3:5]))

	b_date = date(b_year, b_month, b_day)
	a_date = date(a_year, a_month, a_day)

	dt = abs(a_date - b_date)

	return(dt.days/6)
	

def run_bot():
	for comment in r.subreddit("self").comments():

		r1 = re.compile("\d+")
		r2 = re.compile("\d\d\/\d\d\/\d\d\d\d/*")
		t1 = r1.findall(comment.body)
		t2 = r2.findall(comment.body)
		print(t1, t2)
		print(len(t1))
		if "!MucciBot" in comment.body and len(t1) == 1 and not comment.author == r.user.me() and comment.id not in blacklist:
			print("Printing new comment to:", comment.id)
			unitsSac = str(calculate(comment.body)[0])
			unitsTime = str(calculate(comment.body)[1])
			unitsFormat = calculate(comment.body)[2]
			comment.reply("Oh no, Cheetoh!\n\n Based on your request, I have translated " + unitsTime + " " + unitsFormat + " into..... \n\n**~" + unitsSac + " Mooches!** \n\n \n\n ^^This ^^bot ^^is ^^in ^^alpha ^^and ^^was ^^created ^^by ^^a ^^beginner ^^programmer ^^attempting ^^to ^^learn ^^python. ^^Mistakes ^^are ^^inevitable!\n\n **^^^!MucciBot ^^^0000 ^^^days/months/years** \n\n **^^^!MucciBot ^^^mm/dd/yyyy ^^^mm/dd/yyyy**")
			blacklist.append(comment.id)

		if "!MucciBot" in comment.body and len(t2) > 0 and not comment.author == r.user.me() and comment.id not in blacklist:
			print("Printing new comment to:", comment.id)
			difference = str(diff(comment.body))
			comment.reply("Oh no, Cheetoh!\n\n Based on your request, I have translated these two dates into.......  \n\n**~" + difference + " Mooches!** \n\n \n\n ^^This ^^bot ^^is ^^in ^^alpha ^^and ^^was ^^created ^^by ^^a ^^beginner ^^programmer ^^attempting ^^to ^^learn ^^python. ^^Mistakes ^^are ^^inevitable!\n\n **^^^!MucciBot ^^^0000 ^^^days/months/years** \n\nF **^^^!MucciBot ^^^mm/dd/yyyy ^^^mm/dd/yyyy**")
			blacklist.append(comment.id)

		else:
			print("FALSE")

		print("chillin....")
		time.sleep(5)

blacklist = []
while True:
	run_bot()




