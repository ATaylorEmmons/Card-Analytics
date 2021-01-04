
import requests



url = "https://gwent.one/search/ajax"

headers={ 
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',
    }
	
	
data = {
	'v' : '8.0.0',
	'total' : '998',
	'lang' : 'en',
	'page' : '1'
}

req = requests.post(url, data=data, headers=headers);

with open("cardsHtml.html", "w", encoding="utf-8") as outHtml:
	outHtml.write(req.text);