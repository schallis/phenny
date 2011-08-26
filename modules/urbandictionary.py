#!/usr/bin/env python

import web
from lxml.html import parse

uri = 'http://www.urbandictionary.com/define.php?term=%s'

def urbandictionary(word):
	root = parse(uri % word).getroot()
	return ''.join([text for text in root.cssselect('.definition')[0].itertext()])

def urb(phenny, input):
	if not input.group(2):
		return phenny.reply('You done did messed up.')
	word = input.group(2)
	definition = urbandictionary(word)
	if not definition:
		phenny.say('You done made up %s.' % word)
		return

	result = '%s - %s' % (word, definition)
	phenny.say(result)
urb.commands = ['urb']
urb.example = '.urb snaffle'

if __name__ == '__main__':
	print __doc__.strip()
