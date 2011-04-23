#!/usr/bin/env python2

import getpass
import prettytable
from quest import scraper

# Optional configuration. If not set, obtained interactively.
username = None # 'a99bcdef'
password = None # '!@#$%^&*'

def parse_grade(grade):
	"""Suppress all non-integer values."""
	try:
		int(grade)
		return grade
	except ValueError:
		return ''

def make_table(courses, grades):
	pt = prettytable.PrettyTable(["Course", "Grade"])

	for course, grade in zip(courses, grades):
		pt.add_row([course, parse_grade(grade)])

	return pt

# Get any missing credentials.
if not username:
	username = raw_input('Quest username: ')

if not password:
	password = getpass.getpass('Password for %s: ' % (username))

# Go!
qs = scraper.QuestScraper()
qs.login(username, password)
courses, grades = qs.fetch_grades('2')

make_table(courses, grades).printt(header=False, border=False)
