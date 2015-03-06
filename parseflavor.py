#!/usr/bin/env python

import json

# Just FYI!
# White = A, Blue = B, Black = C, Red = D, Green = E, Gold = F, Artifact = G , Unknown = X, Land = Z


# Open the JSON file
jsonfh = open("AllSets.json", "r")

# Load all the cards into a giant dictionary
mtgsets = json.load(jsonfh)

texts = {}

# Okay, we need the colors but in a much shorter format
for mtgset in mtgsets:
	for card in mtgsets[mtgset][u'cards']:
		if u'flavor' in card:
			texts[card[u'flavor']] = card[u'name']

for text in texts.keys():
	card = texts[text]
	print card.encode('utf-8') + ": " + text.encode('utf-8').replace('\n', ' / ')
	# print text.encode('utf-8').replace('\n', ' / ')   # text only
