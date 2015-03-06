#!/usr/bin/env python

import json

# Just FYI!
# White = A, Blue = B, Black = C, Red = D, Green = E, Gold = F, Artifact = G , Unknown = X, Land = Z


# Open the JSON file
jsonfh = open("AllSets.json", "r")

# Load all the cards into a giant dictionary
mtgsets = json.load(jsonfh)

artists = {}

# Okay, we need to cycle through every card
for mtgset in mtgsets:
	for card in mtgsets[mtgset][u'cards']:
		if u'artist' in card:
			if card[u'artist'] in artists:
				artists[card[u'artist']].append(card[u'name'])
			else:
				artists[card[u'artist']] = [card[u'name']]

for artist in sorted(artists.keys()):
	cards = set(artists[artist])
	print str(len(set(artists[artist]))) + "\t" + artist.encode('utf-8')
