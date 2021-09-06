from bs4 import BeautifulSoup
import json

from pprint import pprint

html_doc = open("cardsHtml.html").read();
soup = BeautifulSoup(html_doc, 'html.parser')

#Uses the html file downloaded from "request.py" to take card data and
# convert it to a .json format


#Each card is contained in a card data div tag
cards_html = soup.findAll("div", {"class" : "card-wrap card-data"});

cardList = []

for cardElement in cards_html:
	
	name = cardElement.find("div", {"class" : "card-name"}).find("a").text;
	type = cardElement["data-type"]
	faction = cardElement['data-faction']
	
	power = cardElement['data-power']
	effect = cardElement.find("div", {"class" : "card-body-ability"}).__str__();
	provs = cardElement['data-provision']

	card = {};
	card["name"] = name;
	card["type"] = type;
	card["faction"] = faction;
	
	card["power"] = power;
	card["effect"] = effect;
	card["provisions"] = provs;
	

	
	cardList.append(card);

		
print(str(len(cardList)) + "cards found.")
	


	

with open("gwentCards.json", "w") as outJson:
	outJson.write(json.dumps(cardList, indent=2));
