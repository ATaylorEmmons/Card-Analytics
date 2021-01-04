import json
import numpy as np


def filter_Faction(faction, list):
	return [ card for card in list if card["faction"] == faction ]

def filter_Prov(count, list):
	return [ carte for carte in list if int(carte["provisions"]) == count ]

def filter_Type(cardType, list):
	return [ carte for carte in list if carte['type'] == cardType ]

factions = ["neutral", "nilfgaard", "monster", "northern_realms", "scoiatael", "skellige", "syndicate"]


f = open("gwentCards.json");
cardsJson = f.read();
f.close();

cards = json.loads(cardsJson);



for currentFaction in factions:

	faction = filter_Faction(currentFaction, cards);
	unit = filter_Type("unit", faction);
	
	print(currentFaction);
	print("_______________");
	print("Provisions | Average");

	for provision in range(4, 14):
	
		unitProv = filter_Prov(provision, unit);
		unitPower = np.array([ card['power'] for card in unitProv ]).astype(np.int);
		print(str(provision) + " | " + str(np.average(unitPower)))
	print();

