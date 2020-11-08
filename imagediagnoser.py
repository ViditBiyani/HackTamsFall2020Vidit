import bs4 as bs
import urllib
import requests
conditionList = []
conditionHits = []
searchResults = []
likelyConditions = []

print("What is the link to the image?")
imageLink = input()

googleSearch = "https://images.google.com/searchbyimage?image_url=" + imageLink

url = urllib.request.urlopen('https://www.nhsinform.scot/illnesses-and-conditions/a-to-z').read()
tagsearch = bs.BeautifulSoup(url,'lxml')

for h2 in tagsearch.find_all('h2', class_='module__title'):
	conditionList.append(h2.text)


for i in range(len(conditionList)):
	conditionList[i] = conditionList[i][:-3]

for i in range(len(conditionList)):
	conditionList[i] = conditionList[i][4:]

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
r = requests.get(googleSearch, headers=headers)

soup = bs.BeautifulSoup(r.text,'html5lib')

headings = soup.find_all('h3', class_ = 'LC20lb DKV0Md')

for heading in headings:
    searchResults.append(heading.text)


for condition in conditionList:
	hits = 0
	for search in searchResults:
		if condition.lower() in search.lower():
			hits = hits + 1
	conditionHits.append(hits)
outputCondition = dict(zip(conditionList, conditionHits))


maximum = max(outputCondition.values(), key = lambda v: int(v))

maxkeyarray = [key for key in outputCondition if int(outputCondition[key]) == maximum]

for value in maxkeyarray:
	if maximum != 0:
			if len(maxkeyarray) > 1:
				intro = "You could also have "
			else:
				intro = "You have "
			print(intro + value + ".")
	else:
		print("There was an error")
		break

input("Press Enter to Exit")


