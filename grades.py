#!/usr/bin/env python2

import argparse
import getpass
import prettytable
from quest import scraper
import sys
import time

# Optional configuration. If not set, obtained elsewhere.
username = None # 'a99bcdef'
password = None # '!@#$%^&*'
term = None # '2'

POLL_INTERVAL = 10 * 60 # seconds

def event(bell):
	"""
	Print a newline with an optional bell.
	"""
	if bell:
		print '\x07'
	else:
		print # Only spacing.

def obtain_grades(qs, term, bell, old_courses=None, old_grades=None):
	"""
	Get and output the grades for the given term.
	"""
	courses, grades = qs.fetch_grades(term)

	# If supplied with old information, only print new information if it
	# differs.
	if (not old_courses or not old_grades or courses != old_courses or
			grades != old_grades):
		event(bell)

		pt = prettytable.PrettyTable(['Course', 'Grade'])
		for course, grade in zip(courses, grades):
			pt.add_row([course, grade])
		pt.printt(header=False, border=False)

	return courses, grades

# Get any command-line arguments.
parser = argparse.ArgumentParser(description='Fetch grades from Quest.')
parser.add_argument('--username', help='Quest username')
parser.add_argument('--password', help='Quest password')
parser.add_argument('--term', help='Quest term ID')
parser.add_argument('--loop', action='store_true',
		help='poll for updates regularly until killed')
parser.add_argument('--bell', action='store_true',
		help='print the ASCII bell character when something happens')
args = parser.parse_args()

if args.username:
	username = args.username

if args.password:
	password = args.password

if args.term:
	term = args.term

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
	event(args.bell)
	print e.message
	sys.exit(1)

if not term:
	term_ids, terms = qs.fetch_grade_terms()

	event(args.bell)

	pt = prettytable.PrettyTable(['Id', 'Term'])
	for term_id, term in zip(term_ids, terms):
		pt.add_row([term_id, term])
	pt.printt(border=False)

	term = raw_input('Choose a term: ')

courses, grades = obtain_grades(qs, term, args.bell)

if args.loop:
	while True:
		time.sleep(POLL_INTERVAL)

		courses, grades = obtain_grades(qs, term, args.bell,
				old_courses=courses, old_grades=grades)
