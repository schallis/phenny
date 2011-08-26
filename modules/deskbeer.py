#!/usr/bin/env python

def deskbeer(phenny, word):
    if word == 'when':
        phenny.say('Soon...')
    elif word == 'who':
        phenny.say("Not sure yet. Be nice to me and then we'll see")
    else:
        phenny.say('Pffft......')
deskbeer.commands = ['deskbeer']
deskbeer.example = '.deskbeer'

if __name__ == '__main__':
	print __doc__.strip()
