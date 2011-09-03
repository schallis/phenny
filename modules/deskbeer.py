#!/usr/bin/env python

import datetime

def human_readable_time_left(current_time, deskbeer_time):
	distance_in_time = current_time - deskbeer_time
	distance_in_seconds = int(round(abs(distance_in_time.days * 86400 + distance_in_time.seconds)))
	distance_in_minutes = int(round(distance_in_seconds/60))

	if distance_in_minutes <= 1:
		if include_seconds:
			for remainder in [5, 10, 20]:
				if distance_in_seconds < remainder:
					return "less than %s seconds" % remainder
			if distance_in_seconds < 40:
				return "half a minute"
			elif distance_in_seconds < 60:
				return "less than a minute"
			else:
				return "1 minute"
		else:
			if distance_in_minutes == 0:
				return "less than a minute"
			else return "1 minute"
	elif distance_in_minutes < 45:
		return "%s minutes" % distance_in_minutes
	elif distance_in_minutes < 90:
		return "about 1 hour"
	elif distance_in_minutes < 1440:
		return "about %d hours" % (round(distance_in_minutes / 60.0))

def when():
	current_time = datetime.datetime.now()
	if current_time.isoweekday() == 1:
		return 'Calm down drunkard, it is only Monday afterall!'
	elif current_time.isoweekday() == 2:
		return "Tuesday isn't deskbeer day, but definitely feel less bad going to the pub after work."
	elif current_time.isoweekday() == 3:
		return "We're getting there, only 2 days to go!"
	elif current_time.isoweekday() == 4:
		return "If you're a geek it's games night, if you're not, have fun with the hangover tomorrow. Deskbeer not required."
	elif current_time.isoweekday() == 5:
		deskbeer_time = datetime.datetime(
			current_time.year,
			current_time.month,
			current_time.day,
			17
		)
		if current_time > deskbeer_time:
			return "Deskbeer should be on it's way or in your belly!"
		else:
			time_left = human_readable_time_left(current_time, deskbeer_time)
			return "Deskbeer needs to be aquired in %s" % time_left
	else:
		return "Why are you here on the weekend?"

def who():
	return 'blah'

def db():
	return 'BEEEEEEEEEEEEEEEEER!!!!!'

def deskbeer(phenny, input):
    word = input.group(2)
    functions = {
    	'when': when,
    	'who': who
    }
    if word in functions.keys():
    	reply = functions[word]()
    else:
    	reply = db()
    phenny.say(reply)
deskbeer.commands = ['deskbeer']
deskbeer.example = '.deskbeer'

if __name__ == '__main__':
	print __doc__.strip()
