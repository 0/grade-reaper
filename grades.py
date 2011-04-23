#!/usr/bin/env python2

import getpass
import prettytable
from quest import scraper
import sys

# Optional configuration. If not set, obtained interactively.
username = None # 'a99bcdef'
password = None # '!@#$%^&*'

def make_table(courses, grades):
	pt = prettytable.PrettyTable(["Course", "Grade"])

	for course, grade in zip(courses, grades):
		pt.add_row([course, grade])

	return pt

# Get any missing credentials.
if not username:
	username = raw_input('Quest username: ')

if not password:
	password = getpass.getpass('Password for %s: ' % (username))

# Go!
qs = scraper.QuestScraper(auto_authenticate=True)

try:
	qs.login(username, password)
except scraper.LoginError as e:
	print e.message
	sys.exit(1)

courses, grades = qs.fetch_grades('2')

make_table(courses, grades).printt(header=False, border=False)
