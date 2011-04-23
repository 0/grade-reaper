# grade-reaper

UWaterloo student, want to see what you [failed](http://ugradcalendar.uwaterloo.ca/page/uWaterloo-Grading-System) this term without using the usual [Quest](http://quest.uwaterloo.ca/) interface?

## Setup

### Dependencies

* [prettytable](http://code.google.com/p/prettytable/): `pip install prettytable`
* [scrape-quest](https://github.com/0/scrape-quest): `git submodule update --init` (NB. It has its own dependencies.)

### Configuration

Fill in as much information as you feel comfortable at the top of `grades.py`. Whatever is missing can be provided on the command-line or will be requested interactively.

## Usage

`./grades.py --help`

### Interactive single run

`./grades.py`

Prompts for everything necessary to obtain some grades, and then displays said grades.

### Automated polling

`./grades.py --username a99bcdef --term 2 --loop --bell`

Prompts for the password, and then loops forever, occasionally updating the term 2 grades, with an ASCII bell whenever anything interesting happens.
