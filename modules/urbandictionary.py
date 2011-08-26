#!/usr/bin/env python

import web
from lxml.html import parse

uri = 'http://www.urbandictionary.com/define.php?term=%s'

def urbandictionary(word):
	root = parse(uri % word).getroot()
	return root.cssselect('.definition')[0].text

def ub(phenny, input):
	if not input.group(2):
		return phenny.reply('You done did messed up.')
	word = input.group(2)
	definition = urbandictionary(word)
	if not definition:
		phenny.say('You done made up %s.' % word)
		return

	result = '%s - %s' % (word, definition)
	phenny.say(result)
ub.commands = ['ub']
ub.example = '.ub snaffle'

if __name__ == '__main__':
	print __doc__.strip()