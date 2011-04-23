#!/usr/bin/env python2

import getpass
import prettytable
from quest import scraper
import sys

# Optional configuration. If not set, obtained interactively.
username = None # 'a99bcdef'
password = None # '!@#$%^&*'
term = None # '2'

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

if not term:
	term_ids, terms = qs.fetch_grade_terms()

	pt = prettytable.PrettyTable(['Id', 'Term'])
	for term_id, term in zip(term_ids, terms):
		pt.add_row([term_id, term])
	pt.printt(border=False)

	term = raw_input('Choose a term: ')

courses, grades = qs.fetch_grades(term)

pt = prettytable.PrettyTable(['Course', 'Grade'])
for course, grade in zip(courses, grades):
	pt.add_row([course, grade])
pt.printt(header=False, border=False)
